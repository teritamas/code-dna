import * as vNG from "v-network-graph";

export interface Node extends vNG.Node {
  img: string;
}

export interface Edge extends vNG.Edge {
  name: string;
  diff: number;
  width: number;
  color: string;
  dashed?: boolean;
}

export const initialConfigs = vNG.defineConfigs<Node, Edge>({
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
    gap: 20,
    type: "curve",
    summarize: false,
  },
});
