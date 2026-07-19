<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const password = ref('')
const error = ref('')
const loading = ref(false)
const router = useRouter()
const auth = useAuthStore()

async function submit() {
  error.value = ''
  loading.value = true
  const ok = await auth.login(password.value)
  loading.value = false
  if (ok) {
    router.replace('/')
  } else {
    error.value = 'Wrong password'
    password.value = ''
  }
}
</script>

<template>
  <div class="login-wrap">
    <form class="login-card" @submit.prevent="submit">
      <p class="title">Rover Dashboard</p>
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        class="input"
        autocomplete="current-password"
        autofocus
      />
      <p v-if="error" class="error">{{ error }}</p>
      <button type="submit" class="btn" :disabled="loading">
        {{ loading ? 'Signing in…' : 'Sign in' }}
      </button>
    </form>
  </div>
</template>

<style scoped>
.login-wrap {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #111;
}

.login-card {
  background: #1a1a1a;
  border: 1px solid #2a2a2a;
  border-radius: 12px;
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: 280px;
}

.title {
  font-size: 13px;
  font-weight: 600;
  color: #e8e8e8;
  text-align: center;
  margin-bottom: 4px;
}

.input {
  background: #242424;
  border: 1px solid #2a2a2a;
  border-radius: 8px;
  color: #e8e8e8;
  font-size: 14px;
  padding: 10px 12px;
  outline: none;
  transition: border-color 0.15s;
}

.input:focus {
  border-color: #444;
}

.error {
  font-size: 12px;
  color: #f09595;
  text-align: center;
}

.btn {
  background: #2e2e2e;
  border: 1px solid #3a3a3a;
  border-radius: 8px;
  color: #e8e8e8;
  font-size: 14px;
  padding: 10px;
  cursor: pointer;
  transition: background 0.15s;
  margin-top: 4px;
}

.btn:hover:not(:disabled) {
  background: #383838;
}

.btn:disabled {
  opacity: 0.5;
  cursor: default;
}
</style>
