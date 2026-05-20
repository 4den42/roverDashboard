<script setup>
import { useTelemetryStore } from '../stores/telemetry'

const telemetry = useTelemetryStore()
</script>

<template>
  <div class="telemetry-grid">
    <div class="card">
      <h3>Speed</h3>
      <p>{{ telemetry.speed }} MPH</p>
    </div>

    <div class="card">
      <h3>Battery</h3>
      <p>{{ telemetry.battery }}%</p>
    </div>

    <div class="card">
      <h3>Temperature</h3>
      <p>{{ telemetry.temperature }}°C</p>
 </div>

    <div class="card">
      <h3>Signal</h3>
      <p>{{ telemetry.signalStrength }}%</p>
    </div>
  </div>
</template>

<style scoped>
.telemetry-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
}

.card {
  background: #1e1e1e;
  color: white;
  padding: 1rem;
  border-radius: 12px;
}
</style>
