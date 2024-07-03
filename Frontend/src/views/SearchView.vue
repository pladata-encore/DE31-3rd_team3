<script setup>
import { ref } from 'vue';

const searchbox = ref('');

function searchNews(event) {
  if(event.keyCode === 13) {
    console.log(searchbox.value);
  }
}
</script>

<template>
  <main>
    <h1>뉴스 검색</h1>

    <input type="text" class="searchbox" @keypress="searchNews" v-model="searchbox" placeholder="검색어를 입력하세요.">
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


</style>