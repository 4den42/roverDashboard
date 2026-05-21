<script setup>
import { onMounted, computed } from 'vue'
import { useWebSocket } from '@/composables/useWebSocket'
import { useTelemetryStore } from '@/stores/telemetry'

const store = useTelemetryStore()

const connectionStatus = computed(() => store.connected ? 'green' : 'red')
const connectionText = computed(() => store.connected ? 'Connected' : 'Disconnected')

onMounted(() => {
  useWebSocket()
})
</script>

<template>
  <div class="app">
    <!-- Top Status Bar -->
    <header class="topbar">
      <div class="brand">🚀 Rover Control System</div>
      <div class="status">
        <span :class="['dot', connectionStatus]"></span>
        <span>{{ connectionText }}</span>
      </div>
    </header>
    <!-- Main Content -->
    <main class="main">
      <router-view />
    </main>
  </div>
</template>
