<script setup>
import { onMounted, computed } from 'vue'
import { useWebSocket } from '@/composables/useWebSocket'
import { useTelemetryStore } from '@/stores/telemetry'

const store = useTelemetryStore()
const connectionStatus = computed(() => store.connected ? 'connected' : 'disconnected')
const connectionText = computed(() => store.connected ? 'Connected' : 'Disconnected')

onMounted(() => { useWebSocket() })
</script>

<template>
  <div class="app">
    <header class="topbar">
      <div class="brand">Rover Control System</div>
      <div class="status">
        <span :class="['dot', connectionStatus]"></span>
        <span>{{ connectionText }}</span>
      </div>
    </header>
    <main class="main">
      <router-view />
    </main>
  </div>
</template>

<style>
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 20px;
  background: #141414;
  border-bottom: 1px solid #222;
  position: sticky;
  top: 0;
  z-index: 10;
}

.brand {
  font-size: 14px;
  font-weight: 500;
  color: #e8e8e8;
}

.status {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #666;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #333;
}

.dot.connected { background: #1D9E75; }
.dot.disconnected { background: #E24B4A; }

.main {
  min-height: calc(100vh - 53px);
}
</style>
