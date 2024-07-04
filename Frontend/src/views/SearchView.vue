<script setup>
import { ref } from 'vue';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { Bar } from 'vue-chartjs'

import WordCloud from '../components/WordCloud.vue'
import BarChart from '../components/BarChart.vue'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

const searchbox = ref('');
const chartbox = ref(null);
const wordcloudbox = ref(null);
let count = 0;

function searchNews(event) {
  if (event.keyCode === 13) {
    enableWidgets();
    if (count > 3) {
      // update chart data
      chartbox.value.updateBarChart(
        ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-04', '2024-05-05', '2024-05-06', '2024-05-07'],
        [120, 19, 36, 5, 2, 3, 10],
        searchbox.value
      );
      // update word cloud data
      wordcloudbox.value.updateWordCloud([
        { key: 'asdf', value: 10 },
        { key: 'qwer', value: 9 },
        { key: 'zxcv', value: 8 },
        { key: 'orti', value: 7 },
        { key: 'pndf', value: 6 },
        { key: 'moty', value: 5 },
        { key: 'dfgh', value: 4 },
        { key: 'rtey', value: 3 },
        { key: 'tyui', value: 2 },
      ]);
    }
    count++;
  }
}

function enableWidgets() {
  chartbox.value.$refs.barChart.style.display = 'block';
  wordcloudbox.value.$refs.wordCloudCanvas.style.display = 'block';
}

function getDataFromApi() {
  // code here
}
</script>

<template>
  <main>
    <div class="viewTitle">
      <h1>뉴스 검색</h1>
    </div>

    <div class="viewBody">
      <div class="inputBox">
        <!-- query inputbox -->
        <input type="text" class="searchbox" @keypress="searchNews" v-model="searchbox" placeholder="검색어를 입력하세요.">

        <!-- date inputbox, limit date range 20240501~20240515. default value 20240501 -->
        <input type="date" class="datebox" placeholder="날짜를 입력하세요." min="2024-05-01" max="2024-05-15" value="2024-05-01">
      </div>

      <!-- draw bar chart(initially disabled) -->
      <!-- <Bar ref="chartbox" :data="chart_data" :options="{ responsive: true }" style="display: none"></Bar> -->
      <BarChart ref="chartbox" />
      <WordCloud ref="wordcloudbox" />
    </div>

  </main>
</template>

<style scoped>
h1 {
  margin: 0;
  padding: 1rem;
  text-align: center;
}

main {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.searchbox {
  width: 50%;
  padding: 0.5rem;
  margin: 1rem;
}

.viewTitle {
  background-color: #333;
  color: white;
  width: 100%;
}

.viewBody {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.inputBox {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.inputBox > input {
  margin: 1rem;
  height: 2rem;
}
</style>