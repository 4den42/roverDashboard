import { defineStore } from 'pinia'

export const useTelemetryStore = defineStore('telemetry', {
  state: () => ({
    speed: 0,
    battery: 100,
    temperature: 0,
    signalStrength: 0,
    cpuUsage: 0,
    connected: false
  }),

  actions: {
    updateTelemetry(data) {
      this.speed = data.speed
      this.battery = data.battery
      this.temperature = data.temperature
      this.signalStrength = data.signalStrength
      this.cpuUsage = data.cpuUsage
      this.connected = true
    }
  }
})
