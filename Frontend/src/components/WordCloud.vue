<template>
  <div id="canvasContainer">
    <canvas ref="treeChart" width="600" height="450"></canvas>
  </div>
</template>
<script>
import { ref } from 'vue';

import { Chart } from 'chart.js';
import {TreemapController, TreemapElement} from 'chartjs-chart-treemap';

Chart.register(TreemapController, TreemapElement);

function colorFromRaw(ctx) {
  if (ctx.type !== 'data') {
    return 'transparent';
  }
  const value = ctx.raw.v;
  let alpha = (1 + Math.log(value)) / 5;
  const color = 'green';
  return helpers.color(color)
    .alpha(alpha)
    .rgbString();
}

const data = [
  {name: 'main', value: 1},
  {name: 'main', value: 2},
  {name: 'main', value: 3},
  {name: 'other', value: 4},
  {name: 'other', value: 5},
];

export default {
  data() {
    return this.chartInstance = null;
  },
  mounted() {
    this.renderTreeChart();
  },
  methods: {
    renderTreeChart() {
      const config = {
        type: 'treemap',
        data: {
          datasets: [{
            tree: data,
            key: 'value',
            groups: ['name'],
            backgroundColor: (ctx) => colorFromRaw(ctx),
          }]
        },
        options: {
        }
      }

      const canvas = this.$refs.treeChart;
      this.chartInstance = new Chart(canvas, config);
    },
    updateTreeChart(data) {
      this.chartInstance.data.datasets[0].tree = data;
      this.chartInstance.update();
    },
  },
};
</script>

<style scoped>
div {
  width: 600px;
  height: 350px;
}
</style>
