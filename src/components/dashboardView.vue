<script setup>
import CameraFeed from '../components/CameraFeed.vue'
import TelemetryPanel from '../components/TelemetryPanel.vue'
import ControlPad from '../components/ControlPad.vue'
import { useTelemetryStore } from '../stores/telemetry'
import { onMounted } from 'vue'

const telemetry = useTelemetryStore()

onMounted(() => {
  const socket = new WebSocket('ws://192.168.1.50:8765')

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data)
    telemetry.updateTelemetry(data)
  }
})
</script>

<template>
  <main class="dashboard">
    <div class="top-section">
      <CameraFeed />
    </div>

    <TelemetryPanel />

    <ControlPad />
  </main>
</template>

<style scoped>
.dashboard {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding: 2rem;
  background: #121212;
  min-height: 100vh;
}

.top-section {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 1rem;
}
</style>
