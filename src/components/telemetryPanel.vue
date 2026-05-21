<script setup>
import { useTelemetryStore } from '../stores/telemetry'
const t = useTelemetryStore()
</script>

<template>
  <div class="grid">
    <div class="card">CPU: {{ t.cpu }}%</div>
    <div class="card">RAM: {{ t.ram }}%</div>
    <div class="card">Temp: {{ t.temperature }}°C</div>
    <div class="card">WiFi: {{ t.wifi }} dBm</div>
    <div class="card">Uptime: {{ t.uptime }}s</div>
  </div>
</template>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 10px;
}

.card {
  background: #222;
  color: white;
  padding: 10px;
  border-radius: 10px;
}
</style>
