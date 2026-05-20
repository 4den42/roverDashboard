<script setup>
const streamUrl = 'http://192.168.1.50:8080/video'
</script>

<template>
  <div class="camera-container">
    <img :src="streamUrl" class="camera-feed" />
  </div>
</template>

<style scoped>
.camera-container {
  width: 100%;
  background: #111;
  border-radius: 12px;
  overflow: hidden;
}
.camera-feed {
  width: 100%;
  display: block;
}
</style>
