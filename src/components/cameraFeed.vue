<template>
  <div class="camera">
    <h3>Live Camera</h3>
    <img :src="url" />
  </div>
</template>

<script setup>
const url = "https://raspberrypi.taild8e577.ts.net/camera"
</script>

<style scoped>
.camera img {
  width: 100%;
  border-radius: 10px;
  border: 2px solid #333;
}
</style>
