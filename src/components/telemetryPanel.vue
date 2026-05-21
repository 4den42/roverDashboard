<script setup>
import { useTelemetryStore } from '../stores/telemetry'
const t = useTelemetryStore()
</script>

<template>
  <div class="telemetry">
    <div class="metric">
      <span class="label">CPU</span>
      <span class="value">{{ t.cpu }}<span class="unit">%</span></span>
      <div class="bar"><div class="fill" :style="{ width: t.cpu + '%', background: '#1D9E75' }"></div></div>
    </div>
    <div class="metric">
      <span class="label">RAM</span>
      <span class="value">{{ t.ram }}<span class="unit">%</span></span>
      <div class="bar"><div class="fill" :style="{ width: t.ram + '%', background: '#378ADD' }"></div></div>
    </div>
    <div class="metric">
      <span class="label">Temp</span>
      <span class="value">{{ t.temperature }}<span class="unit">°C</span></span>
      <div class="bar"><div class="fill" :style="{ width: (t.temperature / 85 * 100) + '%', background: '#EF9F27' }"></div></div>
    </div>
    <div class="metric">
      <span class="label">WiFi</span>
      <span class="value">{{ t.wifi }}<span class="unit"> dBm</span></span>
    </div>
    <div class="metric">
      <span class="label">Uptime</span>
      <span class="value">{{ t.uptime }}<span class="unit">s</span></span>
    </div>
  </div>
</template>

<style scoped>
.telemetry {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 10px;
}

.metric {
  background: #1a1a1a;
  border: 1px solid #2a2a2a;
  border-radius: 12px;
  padding: 14px;
}

.label {
  display: block;
  font-size: 11px;
  font-weight: 500;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 6px;
}

.value {
  display: block;
  font-size: 22px;
  font-weight: 500;
  color: #e8e8e8;
}

.unit {
  font-size: 12px;
  color: #555;
  font-weight: 400;
}

.bar {
  height: 3px;
  background: #2a2a2a;
  border-radius: 2px;
  margin-top: 10px;
  overflow: hidden;
}

.fill {
  height: 100%;
  border-radius: 2px;
  transition: width 0.5s ease;
}
</style>
