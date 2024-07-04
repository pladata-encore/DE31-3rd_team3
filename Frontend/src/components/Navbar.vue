<template>
  <h1>뉴스 분석 플랫폼</h1>
  <nav>
    <ul>
      <li><a href="/">메인 화면</a></li>
      <li><a href="/monthly">월간 뉴스</a></li>
      <li><a href="/weekly">주간 뉴스</a></li>
      <li><a href="/daily">일간 뉴스</a></li>
      <li><a href="/search">뉴스 검색</a></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  // Add your component logic here
}
</script>

<style scoped>
h1 {
  margin: 0;
  padding: 1rem;
  text-align: center;
}

nav {
  background-color: #333;
  color: white;
  padding: 1rem;
}

ul {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
}

li {
  margin: 0 1rem;
  color: white;
}
</style>