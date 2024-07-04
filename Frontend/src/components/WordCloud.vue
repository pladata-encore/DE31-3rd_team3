<template>
  <div>
    <canvas ref="wordCloudCanvas" style="display: none;"></canvas>
  </div>
</template>

<script>
import { Chart } from 'chart.js';
import { WordCloudController, WordElement } from 'chartjs-chart-wordcloud';

Chart.register(WordCloudController, WordElement);

export default {
  data() {
    return this.wordCloudInstance = null;
  },
  mounted() {
    this.renderWordCloud();
  },
  methods: {
    renderWordCloud() {
      const words = [
        { key: 'word', value: 10 },
        { key: 'words', value: 8 },
        { key: 'cloud', value: 6 },
        { key: 'chart', value: 4 },
        { key: 'js', value: 2 },
        { key: 'vue', value: 1 }
      ];

      const data = {
        labels: words.map((d) => d.key),
        datasets: [
          {
            label: '',
            data: words.map((d) => 10 + d.value * 7),
          },
        ],
      };

      const config = {
        type: 'wordCloud',
        data: data,
        options: {
          plugins: {
            legend: {
              display: false,
            },
          },
        },
      }

      const canvas = this.$refs.wordCloudCanvas;
      this.wordCloudInstance = new Chart(canvas, config);
    },
    updateWordCloud(words) {
      this.wordCloudInstance.data.labels = words.map((d) => d.key);
      this.wordCloudInstance.data.datasets[0].data = words.map((d) => 10 + d.value * 7);
      this.wordCloudInstance.update();
    },
  },
};
</script>

<style scoped>
div {
  width: 100%;
  height: 30rem;
}
</style>
