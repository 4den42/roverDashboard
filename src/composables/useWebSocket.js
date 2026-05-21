import { useTelemetryStore } from '@/stores/telemetry'

export function useWebSocket() {
  const store = useTelemetryStore()
  const ws = new WebSocket(`wss://${window.location.host}/ws/telemetry`)

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data)
    store.updateTelemetry(data)
  }

  ws.onclose = () => {
    store.connected = false
  }

  return { ws }
}
