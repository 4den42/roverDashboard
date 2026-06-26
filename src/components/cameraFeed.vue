<template>
  <div class="camera">
    <img :src="url" />
  </div>
</template>

<script setup>
const url = `${window.location.protocol}//${window.location.host}/camera`
</script>

<style scoped>
.camera img {
  width: 100%;
  border-radius: 10px;
  border: 2px solid #333;
}
</style>
