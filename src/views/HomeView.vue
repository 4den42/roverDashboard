<script setup>
import { onMounted } from 'vue'
import CameraFeed from '../components/cameraFeed.vue'
import TelemetryPanel from '../components/telemetryPanel.vue'
import ControlPad from '../components/controlPad.vue'
import { useTelemetryStore } from '../stores/telemetry'

const telemetry = useTelemetryStore()

onMounted(() => {
  const socket = new WebSocket("ws://100.78.160.76:8000/ws/telemetry")

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data)
    telemetry.updateTelemetry(data)
  }

  socket.onopen = () => {
    console.log("Connected to rover 🚀")
  }

  socket.onclose = () => {
    console.log("Disconnected from rover ❌")
  }
})
</script>

<template>
  <div class="dashboard">
    <h1>Rover Control Dashboard</h1>

    <div class="top">
      <CameraFeed />
      <TelemetryPanel />
    </div>

    <ControlPad />
  </div>
</template>

<style scoped>
.dashboard {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  background: #111;
  color: white;
  min-height: 100vh;
}

.top {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
}
</style>
