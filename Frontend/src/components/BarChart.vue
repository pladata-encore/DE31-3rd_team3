<template>
  <div>
    <canvas ref="barChart" style="display: none"></canvas>
  </div>
</template>

<script>
import { ref } from 'vue';
import {
  Chart,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { Bar } from 'vue-chartjs'
Chart.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

function renderBarChart(labelList, dataList, query) {
  const labels = ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-04', '2024-05-05', '2024-05-06', '2024-05-07'];
  const data = [12, 19, 3, 5, 2, 3, 10];
  const chart_option = {
    type: 'bar',
    data: {
      labels: labelList,
      datasets: [
        {
          label: query,
          data: dataList,
          backgroundColor: [
            'rgba(255, 99, 132, 0.5)',
            'rgba(54, 162, 235, 0.5)',
            'rgba(255, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgba(153, 102, 255, 0.5)',
            'rgba(255, 159, 64, 0.5)',
            'rgba(255, 99, 132, 0.5)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)',
            'rgba(255, 99, 132, 1)'
          ],
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      },
      responsive: true,
    }
  }

  const canvas = this.$refs.barChart;
  new Chart(canvas, chart_option);
}

export default {
  data() {
    return this.chartInstance = null;
  },
  mounted() {
    this.renderBarChart();
  },
  methods: {
    renderBarChart() {
      const labels = ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-04', '2024-05-05', '2024-05-06', '2024-05-07'];
      const data = [12, 19, 3, 5, 2, 3, 10];
      const chart_option = {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [
            {
              label: "query",
              data: data,
              backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(255, 159, 64, 0.5)',
                'rgba(255, 99, 132, 0.5)'
              ],
              borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)'
              ],
            }
          ]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          },
          responsive: true,
        }
      }

      const canvas = this.$refs.barChart;
      this.chartInstance = new Chart(canvas, chart_option);
    },
    updateBarChart(labelList, dataList, query) {
      // update data
      this.chartInstance.data.datasets[0].data = dataList;
      this.chartInstance.data.labels = labelList;
      this.chartInstance.data.datasets[0].label = query;
      this.chartInstance.update();
    }
  },

}
</script>

<style scoped>
div {
  width: 100%;
  height: 30rem;
}
</style>