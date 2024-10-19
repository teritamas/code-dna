<script setup lang="ts">
import { reactive } from "vue";
import * as vNG from "v-network-graph";

interface Node extends vNG.Node {
  img: string;
}

interface Edge extends vNG.Edge {
  width: number;
  color: string;
  dashed?: boolean;
}

const nodes: Record<string, Node> = {
  node1: { name: "佐藤", img: "url.png" },
  node2: { name: "鈴木", img: "url.png" },
  node3: { name: "田中", img: "url.png" },
  node4: { name: "高橋", img: "url.png" },
  node5: { name: "森", img: "url.png" },
};

const edges: Record<string, Edge> = {
  edge1: { source: "node2", target: "node5", width: 1, color: "red" },
  edge2: { source: "node2", target: "node3", width: 1, color: "blue" },
  edge3: { source: "node3", target: "node4", width: 1, color: "blue" },
  edge4: {
    source: "node3",
    target: "node4",
    width: 1,
    color: "rgb(222 156 7)",
  },
  edge5: { source: "node4", target: "node5", width: 1, color: "red" },
  edge6: { source: "node4", target: "node5", width: 1, color: "blue" },
  edge7: {
    source: "node4",
    target: "node5",
    width: 1,
    color: "rgb(222 156 7)",
  },
  edge8: { source: "node4", target: "node5", width: 1, color: "green" },
};

const layouts = {
  nodes: {
    node1: { x: 0, y: 0 },
    node2: { x: 80, y: 80 },
    node3: { x: 160, y: 0 },
    node4: { x: 240, y: 80 },
    node5: { x: 320, y: 0 },
  },
};

const initialConfigs = vNG.defineConfigs<Node, Edge>({
  node: {
    selectable: true,
    normal: {
      type: "circle",
      radius: 32,
      strokeWidth: 0,
      strokeColor: "#000000",
      strokeDasharray: "0",
      color: "#4466cc",
    },
    hover: {
      type: "circle",
      radius: 38,
      strokeWidth: 0,
      strokeColor: "#000000",
      strokeDasharray: "0",
      color: "#dd2288",
    },
    selected: {
      type: "circle",
      radius: 38,
      strokeWidth: 0,
      strokeColor: "#000000",
      strokeDasharray: "0",
      color: "#4466cc",
    },
    label: {
      visible: true,
      fontFamily: undefined,
      fontSize: 11,
      lineHeight: 1.1,
      color: "#000000",
      margin: 4,
      direction: "south",
      background: {
        visible: false,
        color: "#ffffff",
        padding: {
          vertical: 1,
          horizontal: 4,
        },
        borderRadius: 2,
      },
    },
    focusring: {
      visible: true,
      width: 4,
      padding: 3,
      color: "#eebb00",
      dasharray: "0",
    },
  },
  edge: {
    selectable: true,
    normal: {
      width: (edge) => edge.width, // Use the value of each edge object
      color: (edge) => edge.color,
      dasharray: "0",
      linecap: "butt",
      animate: false,
      animationSpeed: 50,
    },
    hover: {
      width: 4,
      color: (edge) => edge.color,
      dasharray: "0",
      linecap: "butt",
      animate: false,
      animationSpeed: 50,
    },
    selected: {
      width: 3,
      color: (edge) => edge.color,
      dasharray: "6",
      linecap: "round",
      animate: true,
      animationSpeed: 50,
    },
    gap: 3,
    type: "curve",
    summarize: false,
  },
});
const configs = reactive(initialConfigs);

import { EventHandlers } from "v-network-graph";
const eventHandlers: EventHandlers = {
  "node:click": ({ node, event }) => {
    console.log("click");
    console.log(node);
  },
};
const title = ref("マップ - CodeDNA");
useHead({
  title,
});
</script>

<template>
  <ClientOnly>
    <div class="p-12 max-lg:p-4">
      <GlowBorder
        class="relative flex h-[500px] w-full flex-col items-center justify-center overflow-hidden rounded-lg border bg-background md:shadow-xl"
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
            <!-- circle for filling background -->
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
              :xlink:href="`./faces/${nodes[nodeId].url}`"
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
      </GlowBorder>
    </div>
  </ClientOnly>
</template>
