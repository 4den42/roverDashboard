import { defineStore } from 'pinia'

export const useTelemetryStore = defineStore('telemetry', {
  state: () => ({
    cpu: 0,
    ram: 0,
    temperature: 0,
    wifi: 0,
    uptime: 0,
    eth_rx: 0,
    eth_tx: 0,
    connected: false
  }),

  actions: {
    updateTelemetry(data) {
      this.cpu = data.cpu
      this.ram = data.ram
      this.temperature = data.temperature
      this.wifi = data.wifi
      this.uptime = data.uptime
      this.eth_rx = data.eth_rx
      this.eth_tx = data.eth_tx
      this.connected = true
    }
  }
})
