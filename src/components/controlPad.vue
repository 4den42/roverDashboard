<script setup>
const send = async (command) => {
  await fetch('/api/control', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ command })
  })
}
</script>

<template>
  <div class="controls-wrap">
    <p class="section-label">Controls</p>
    <div class="dpad">
      <button class="btn" style="grid-column:2;grid-row:1" @click="send('forward')">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
      </button>
      <button class="btn" style="grid-column:1;grid-row:2" @click="send('left')">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>
      </button>
      <button class="btn btn-stop" style="grid-column:2;grid-row:2" @click="send('stop')">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="6" y="6" width="12" height="12" rx="1"/></svg>
      </button>
      <button class="btn" style="grid-column:3;grid-row:2" @click="send('right')">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </button>
      <button class="btn" style="grid-column:2;grid-row:3" @click="send('backward')">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
      </button>
    </div>
  </div>
</template>

<style scoped>
.controls-wrap {
  background: #1a1a1a;
  border: 1px solid #2a2a2a;
  border-radius: 12px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.section-label {
  font-size: 11px;
  font-weight: 500;
  color: #666;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 16px;
  align-self: flex-start;
}

.dpad {
  display: grid;
  grid-template-columns: repeat(3, 52px);
  grid-template-rows: repeat(3, 52px);
  gap: 8px;
}

.btn {
  background: #242424;
  border: 1px solid #2a2a2a;
  border-radius: 10px;
  color: #e8e8e8;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s, transform 0.1s;
}

.btn:hover { background: #2e2e2e; }
.btn:active { transform: scale(0.95); }

.btn-stop {
  background: rgba(162, 45, 45, 0.2);
  border-color: rgba(162, 45, 45, 0.4);
  color: #f09595;
}

.btn-stop:hover { background: rgba(162, 45, 45, 0.3); }
</style> 
