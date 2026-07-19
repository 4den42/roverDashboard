import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    checked: false,
    authenticated: false,
  }),

  actions: {
    async check() {
      try {
        const res = await fetch('/api/auth/check')
        this.authenticated = res.ok
      } catch {
        this.authenticated = false
      }
      this.checked = true
    },

    async login(password: string): Promise<boolean> {
      const res = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password }),
      })
      if (res.ok) {
        this.authenticated = true
        return true
      }
      return false
    },

    async logout() {
      await fetch('/api/logout', { method: 'POST' })
      this.authenticated = false
    },
  },
})
