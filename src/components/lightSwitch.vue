<script setup>
import { ref, onMounted } from 'vue'

const on = ref(false)

onMounted(async () => {
  const res = await fetch('/api/light')
  if (res.ok) {
    const data = await res.json()
    on.value = data.state
  }
})

const toggle = async () => {
  const next = !on.value
  const res = await fetch('/api/light', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ state: next })
  })
  if (res.ok) on.value = next
}
</script>

<template>
  <div class="light-wrap">
    <p class="section-label">Light</p>
    <div class="switch-body" @click="toggle" :class="{ on }">
      <div class="glow" v-if="on" />
      <div class="dial">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
          <path d="M12 2v2M12 20v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M2 12h2M20 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>
          <circle cx="12" cy="12" r="4"/>
        </svg>
      </div>
      <span class="state-text">{{ on ? 'ON' : 'OFF' }}</span>
    </div>
  </div>
</template>

<style scoped>
.light-wrap {
  background: #1a1a1a;
  border: 1px solid #2a2a2a;
  border-radius: 12px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
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

.switch-body {
  position: relative;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: #242424;
  border: 2px solid #2a2a2a;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
  cursor: pointer;
  transition: border-color 0.2s, background 0.2s;
  user-select: none;
}

.switch-body:hover {
  background: #2a2a2a;
}

.switch-body:active {
  transform: scale(0.95);
}

.switch-body.on {
  border-color: #f5c842;
  background: rgba(245, 200, 66, 0.08);
}

.glow {
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(245, 200, 66, 0.18) 0%, transparent 70%);
  pointer-events: none;
}

.dial {
  color: #555;
  transition: color 0.2s;
}

.switch-body.on .dial {
  color: #f5c842;
}

.state-text {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: #555;
  transition: color 0.2s;
}

.switch-body.on .state-text {
  color: #f5c842;
}
</style>
