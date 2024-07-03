<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
</script>

<template>
  <header>
    <div class="wrapper">
      <Navbar />
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
body {
  font-family: Arial, sans-serif;
  margin: 0;
}

header {
  background-color: #333;
  color: white;
  padding: 1rem;
}
</style>