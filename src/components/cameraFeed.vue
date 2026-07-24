<template>
  <div class="camera">
    <img v-if="!error" :src="url" @error="error = true" />
    <div v-else class="unavailable">Camera unavailable</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const url = `${window.location.protocol}//${window.location.host}/camera`
const error = ref(false)
</script>

<style scoped>
.camera img {
  width: 100%;
  border-radius: 10px;
  border: 2px solid #333;
}

.unavailable {
  width: 100%;
  aspect-ratio: 4/3;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #555;
  font-size: 13px;
  border-radius: 10px;
  border: 2px solid #333;
}
</style>
