import { useTelemetryStore } from '@/stores/telemetry'

let ws = null
let reconnectTimer = null

function connect() {
  const store = useTelemetryStore()
  const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:'
  ws = new WebSocket(`${protocol}//${window.location.host}/ws/telemetry`)

  ws.onopen = () => {
    store.connected = true
  }

  ws.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data)
      store.updateTelemetry(data)
    } catch {
      // ignore malformed frames
    }
  }

  ws.onerror = () => {
    store.connected = false
    // browser closes the socket after an error; onclose handles reconnect
  }

  ws.onclose = () => {
    store.connected = false
    clearTimeout(reconnectTimer)
    reconnectTimer = setTimeout(connect, 3000)
  }
}

export function useWebSocket() {
  if (!ws || ws.readyState === WebSocket.CLOSED || ws.readyState === WebSocket.CLOSING) {
    clearTimeout(reconnectTimer)
    connect()
  }
}

if (import.meta.hot) {
  import.meta.hot.dispose(() => {
    clearTimeout(reconnectTimer)
    ws?.close()
    ws = null
  })
}
