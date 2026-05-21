<script setup>
const send = async (command) => {
  await fetch('/api/control', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ command })
  });
};
</script>
<template>
  <div class="controls">
    <button @click="sendCommand('forward')">Forward</button>

    <div class="middle-row">
      <button @click="sendCommand('left')">Left</button>
      <button @click="sendCommand('stop')">Stop</button>
      <button @click="sendCommand('right')">Right</button>
    </div>

    <button @click="sendCommand('backward')">Backward</button>
  </div>
</template>

<style scoped>
.controls {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.middle-row {
  display: flex;
  gap: 1rem;
}

button {
  padding: 1rem;
  border: none;
  border-radius: 10px;
  background: #2c2c2c;
  color: white;
  cursor: pointer;
}

button:hover {
  background: #3c3c3c;
}
</style>
