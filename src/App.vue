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

    <!-- Footer -->
    <footer class="footer">
      <span>Rover Dashboard v1.0</span>
      <span>Pi Live Control Interface</span>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const connectionStatus = ref('offline')
const connectionText = ref('Disconnected')

// Simple heartbeat (can later be tied to WebSocket)
onMounted(() => {
  setTimeout(() => {
    connectionStatus.value = 'online'
    connectionText.value = 'Connected'
  }, 1000)
})
</script>

<style scoped>
.app {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: #0f1115;
  color: #eaeaea;
  font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
}

/* Top bar */
.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 18px;
  background: #151923;
  border-bottom: 1px solid #2a2f3a;
}

.brand {
  font-weight: 600;
  letter-spacing: 0.5px;
}

/* Connection indicator */
.status {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.dot.online {
  background: #3cff7a;
  box-shadow: 0 0 8px #3cff7a;
}

.dot.offline {
  background: #ff4d4d;
  box-shadow: 0 0 8px #ff4d4d;
}

/* Main area */
.main {
  flex: 1;
  padding: 16px;
  overflow: auto;
}

/* Footer */
.footer {
  display: flex;
  justify-content: space-between;
  padding: 10px 18px;
  font-size: 12px;
  color: #888;
  border-top: 1px solid #2a2f3a;
  background: #151923;
}
</style>
