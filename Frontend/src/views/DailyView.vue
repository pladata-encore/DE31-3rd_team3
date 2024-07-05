<script setup>
import { ref, nextTick } from 'vue';
import axios from 'axios';

import WordCloud from '../components/WordCloud.vue'

async function getDataFromApi(target_api, params) {
  const url = `http://140.238.153.4:21080/api/v1/${target_api}`;
  return axios.get(url, { params });
}

const start_date_picker = ref(null);
const end_date_picker = ref(null);
const wordcloudbox = ref(null);

function searchNews(event) {
  // get value of datepicker
  const start_date = start_date_picker.value.value;
  const end_date = end_date_picker.value.value;
  
  console.log(start_date, end_date);
  if (start_date === '' || end_date === '') {
    alert('날짜를 입력하세요.');
    return;
  } else if (start_date > end_date) {
    alert('시작 날짜가 종료 날짜보다 늦습니다.');
    return;
  } else if (end_date > '2024-05-22') {
    alert('종료 날짜가 2024-05-22보다 늦습니다.');
    return;
  }
  // enableWidgets();
  // wordcloudbox.value.renderWordCloud();

  // get data from api
  getDataFromApi('news_betwn_range', { start_date, end_date })
    .then((response) => {
      console.log(response);
      // wordcloudbox.value.updateWordCloudImage(res);
      // wordcloudbox.value.reRenderWordCloud(response.data.data);
    })
    .catch((error) => {
      console.error(error);
    })
}

function enableWidgets() {
  wordcloudbox.value.$refs.wordCloudCanvas.style.display = 'block';
}
</script>

<template>
  <main>
    <div class="viewTitle">
      <h1>기간별 토픽 조회</h1>
    </div>

    <div class="viewBody">
      <div class="inputBox">
        <!-- daterange inputbox, limit date range 20240501~20240522. default value 20240501 -->
        <input ref="start_date_picker" type="date" class="st_datebox" placeholder="시작 날짜를 입력하세요." min="2024-05-01" max="2024-05-22" value="2024-05-01">
        <input ref="end_date_picker" type="date" class="ed_datebox" placeholder="종료 날짜를 입력하세요." min="2024-05-01" max="2024-05-22" value="2024-05-22">

        <!-- search button -->
        <button @click="searchNews">검색</button>
      </div>

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