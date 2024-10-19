<script setup lang="ts">
import * as vNG from "v-network-graph";
import { useMouse } from "@vueuse/core";
import {
  initialConfigs,
  type Edge,
  type Node,
} from "~/lib/network-graph-config";

const client = useSupabaseClient();
const userId = ref("");

// ネットワークグラフ描画の初期設定
const configs = reactive(initialConfigs);
const nodes: Ref<Record<string, Node>> = ref({});
const edges: Ref<Record<string, Edge>> = ref({});

// グラフのクリック時のイベント
const eventHandlers: vNG.EventHandlers = {
  "node:pointerover": ({ node }) => {
    targetNodeId.value = node;
    nodeTooltipOpacity.value = 1; // show
  },
  "node:pointerout": (_) => {
    nodeTooltipOpacity.value = 0; // hide
  },
  "edge:pointerover": ({ edge }) => {
    targetEdgeId.value = edge ?? "";
    edgeTooltipOpacity.value = 1; // show
  },
  "edge:pointerout": (_) => {
    edgeTooltipOpacity.value = 0; // hide
  },
};
const title = ref("マップ - CodeDNA");
useHead({
  title,
});

onMounted(async () => {
  const user = await client.auth.getUser();
  // 認証されていない時、ログインページにリダイレクト
  if (!user) {
    client.auth.signOut();
    window.location.href = "/login";
  }

  // 認証されている場合はユーザー情報を取得
  userId.value = user.data.user?.id!;
  await fetchMapRelation();

  // 5秒ごとにデータを取得
  setInterval(async () => {
    await fetchMapRelation();
  }, 10000);
});

// DBからデータを取得し、ノードとエッジを作成
const fetchMapRelation = async () => {
  const { data, error } = await client.from("code_dna_summary").select(`
      *,
      profiles(*)
  `);

  let tempData = data;

  // EdgesとNodesを作成
  data?.map((item: any) => {
    // ユーザ情報を利用して、ノードを作成
    const newNode = {
      [item.profiles.id]: {
        name: item.profiles.user_name,
        img: item.profiles.avatar_url,
      },
    };
    nodes.value = { ...nodes.value, ...newNode };

    // tempDataからitemを削除
    tempData = tempData?.filter((other: any) => other.id !== item.id) ?? [];

    // 類似度を計算してエッジを作成
    tempData?.map((tempDataTarget: any) => {
      // 絶対値が0.1未満の場合は同じノードとみなす
      const variable_name_simplicity_rate_diff = Math.abs(
        item.variable_name_simplicity_rate -
          tempDataTarget.variable_name_simplicity_rate
      );
      if (variable_name_simplicity_rate_diff <= 0.4) {
        const newEdge = {
          [`${item.id}-${tempDataTarget}-variable_name_simplicity_rate`]: {
            name: "変数名の付け方",
            diff: variable_name_simplicity_rate_diff,
            source: item.profiles.id,
            target: tempDataTarget.profiles.id,
            width: 1,
            color: "blue",
          },
        };
        edges.value = { ...edges.value, ...newEdge };
      }
      const method_splitting_coarseness_rate_diff = Math.abs(
        item.method_splitting_coarseness_rate -
          tempDataTarget.method_splitting_coarseness_rate
      );
      if (method_splitting_coarseness_rate_diff <= 0.4) {
        const newEdge = {
          [`${item.id}-${tempDataTarget}-method_splitting_coarseness_rate`]: {
            name: "メソッドの分割粒度",
            diff: method_splitting_coarseness_rate_diff,
            source: item.profiles.id,
            target: tempDataTarget.profiles.id,
            width: 1,
            color: "red",
          },
        };
        edges.value = { ...edges.value, ...newEdge };
      }
      const processing_intent_communicating_rate_diff = Math.abs(
        item.processing_intent_communicating_rate -
          tempDataTarget.processing_intent_communicating_rate
      );
      if (processing_intent_communicating_rate_diff <= 0.4) {
        const newEdge = {
          [`${item.id}-${tempDataTarget}-processing_intent_communicating_rate`]:
            {
              name: "処理の意図を伝える手段",
              diff: processing_intent_communicating_rate_diff,
              source: item.profiles.id,
              target: tempDataTarget.profiles.id,
              width: 1,
              color: "green",
            },
        };
        edges.value = { ...edges.value, ...newEdge };
      }
      const commit_granularity_rate_diff = Math.abs(
        item.commit_granularity_rate - tempDataTarget.commit_granularity_rate
      );
      if (commit_granularity_rate_diff <= 0.4) {
        const newEdge = {
          [`${item.id}-${tempDataTarget}-commit_granularity_rate`]: {
            name: "コミットの粒度",
            diff: commit_granularity_rate_diff,
            source: item.profiles.id,
            target: tempDataTarget.profiles.id,
            width: 1,
            color: "yellow",
          },
        };
        edges.value = { ...edges.value, ...newEdge };
      }
    });
  });
};

// エッジにマウスポインターが乗った時の処理
const tooltipPos = ref({ left: "0px", top: "0px" });
const targetEdgeId = ref("");
const edgeTooltipOpacity = ref(0); // 0 or 1
const edgeTooltip = ref<HTMLDivElement>();

const targetNodeId = ref<string>("");
const nodeTooltipOpacity = ref(0); // 0 or 1
const nodeTooltip = ref<HTMLDivElement>();

const { x, y } = useMouse();

// エッジにマウスポインターが乗った時、ポインターを起点としてtooltipを表示
watch(
  [edgeTooltipOpacity, nodeTooltipOpacity],
  () => {
    // ポインターのxy座標を取得
    tooltipPos.value = {
      left: x.value - 100 + "px",
      top: y.value - 200 + "px",
    };
  },
  { deep: true }
);
</script>

<template>
  <ClientOnly>
    <div class="p-12 max-lg:p-4 tooltip-wrapper">
      <GlowBorder
        class="relative flex h-[80vh] w-full flex-col items-center justify-center overflow-hidden rounded-lg border bg-background md:shadow-xl"
        :color="['#A07CFE', '#FE8FB5', '#FFBE7B']"
      >
        <v-network-graph
          :nodes="nodes"
          :edges="edges"
          :configs="configs"
          :event-handlers="eventHandlers"
        >
          <defs>
            <clipPath id="faceCircle" clipPathUnits="objectBoundingBox">
              <circle cx="0.5" cy="0.5" r="0.5" />
            </clipPath>
          </defs>

          <!-- Replace the node component -->
          <template #override-node="{ nodeId, scale, config, ...slotProps }">
            <circle
              class="face-circle"
              :r="config.radius * scale"
              fill="#ffffff"
              v-bind="slotProps"
            />
            <image
              class="face-picture"
              :x="-config.radius * scale"
              :y="-config.radius * scale"
              :width="config.radius * scale * 2"
              :height="config.radius * scale * 2"
              :xlink:href="`${nodes[nodeId].img}`"
              clip-path="url(#faceCircle)"
            />
            <circle
              class="face-circle"
              :r="config.radius * scale"
              fill="none"
              stroke="#808080"
              :stroke-width="1 * scale"
              v-bind="slotProps"
            />
          </template>
        </v-network-graph>

        <!-- NodeのTooltip -->
        <div
          ref="nodeTooltip"
          class="nodeTooltip"
          :style="{ ...tooltipPos, opacity: nodeTooltipOpacity }"
        >
          <div>類似項目: {{ `${nodes[targetNodeId]}` }}<br /></div>
        </div>

        <!-- EdgeのTooltip -->
        <div
          ref="edgeTooltip"
          class="edgeTooltip"
          :style="{ ...tooltipPos, opacity: edgeTooltipOpacity }"
        >
          <div>
            類似項目: {{ `${edges[targetEdgeId]?.name ?? ""}` }}<br />
            類似度: {{ `${(edges[targetEdgeId]?.diff * 100).toFixed(1)}` }}%
          </div>
        </div>
      </GlowBorder>
    </div>
  </ClientOnly>
</template>

<style lang="css" scoped>
.tooltip-wrapper {
  position: relative;
}
.edgeTooltip {
  top: 0;
  left: 0;
  opacity: 0;
  position: absolute;
  width: 120px;
  height: 100px;
  display: grid;
  place-content: center;
  text-align: center;
  font-size: 12px;
  background-color: #fff0bd;
  border: 1px solid #ffb950;
  box-shadow: 2px 2px 2px #aaa;
  transition: opacity 0.2s linear;
  pointer-events: none;
}
.nodeTooltip {
  top: 0;
  left: 0;
  opacity: 0;
  position: absolute;
  width: 120px;
  height: 100px;
  display: grid;
  place-content: center;
  text-align: center;
  font-size: 12px;
  background-color: #fff0bd;
  border: 1px solid #ffb950;
  box-shadow: 2px 2px 2px #aaa;
  transition: opacity 0.2s linear;
  pointer-events: none;
}
</style>
