<script setup>
import { ref } from 'vue';
import axios from 'axios';

import BarChart from '../components/BarChart.vue'

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

async function getDataFromApi(target_api, params) {
  const url = `http://140.238.153.4:21080/api/v1/${target_api}`;
  return axios.get(url, { params });
}

const searchbox = ref('');
const chartbox = ref(null);

function searchNews(event) {
  if (event.keyCode === 13) {
    enableWidgets();

    // get value of datepicker
    const current_date = document.querySelector('.datebox').value;

    // get data from api
    getDataFromApi('search_news', { keyword: searchbox.value, date: current_date})
      .then((response) => {
        const res = response.data.data;
        const labels = res.map((item) => item.datetime);
        const values = res.map((item) => item.frequency);
        chartbox.value.updateBarChart(labels, values, searchbox.value);
      })
      .catch((error) => {
        console.error(error);
      });
  }
}

function enableWidgets() {
  chartbox.value.$refs.barChart.style.display = 'block';
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
        <input type="date" class="datebox" placeholder="날짜를 입력하세요." min="2024-05-01" max="2024-05-28" value="2024-05-01">

      </div>

      <!-- draw bar chart(initially disabled) -->
      <!-- <Bar ref="chartbox" :data="chart_data" :options="{ responsive: true }" style="display: none"></Bar> -->
      <BarChart ref="chartbox" />
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
  width: 50vw;
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