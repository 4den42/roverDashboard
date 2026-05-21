<template>
  <div class="camera">
    <h3>Live Camera</h3>
    <img :src="url" />
  </div>
</template>

<script setup>
const url = "http://100.78.160.76:8000/camera"
</script>

<style scoped>
.camera img {
  width: 100%;
  border-radius: 10px;
  border: 2px solid #333;
}
</style>
