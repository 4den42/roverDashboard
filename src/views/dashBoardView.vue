<template>
  <div class="dashboard">
    <div class="section-label">Telemetry</div>
    <TelemetryPanel class="mb" />

    <div class="content">
      <div class="camera-card">
        <div class="card-header">Live camera</div>
        <CameraFeed />
      </div>
      <div class="right-col">
        <ControlPad />
        <LightSwitch />
      </div>
    </div>
  </div>
</template>

<script setup>
import CameraFeed from '../components/cameraFeed.vue'
import TelemetryPanel from '../components/telemetryPanel.vue'
import ControlPad from '../components/controlPad.vue'
import LightSwitch from '../components/lightSwitch.vue'
</script>

<style scoped>
.dashboard {
  padding: 16px;
  max-width: 960px;
  margin: 0 auto;
}

.section-label {
  font-size: 11px;
  font-weight: 500;
  color: #555;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 10px;
}

.mb { margin-bottom: 16px; }

.content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 16px;
}

.camera-card {
  background: #1a1a1a;
  border: 1px solid #2a2a2a;
  border-radius: 12px;
  overflow: hidden;
}

.card-header {
  font-size: 11px;
  border-bottom: 1px solid #2a2a2a;
  padding: 12px 14px;
  font-weight: 500;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #555;
}

.right-col {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

@media (max-width: 600px) {
  .content {
    grid-template-columns: 1fr;
  }
}
</style>
