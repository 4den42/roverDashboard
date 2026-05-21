<template>
  <div class="dashboard">
    <h1>Rover Dashboard</h1>

    <div class="grid">
      <CameraFeed />
      <TelemetryPanel />
    </div>

    <ControlPad />
  </div>
</template>

<script setup>
import CameraFeed from '../components/cameraFeed.vue'
import TelemetryPanel from '../components/telemetryPanel.vue'
import ControlPad from '../components/controlPad.vue'
</script>

<style scoped>
.dashboard {
  padding: 20px;
  color: white;
  background: #111;
  min-height: 100vh;
}

.grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
  margin-bottom: 20px;
}
</style>
