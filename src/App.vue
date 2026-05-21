<template>
  <div class="app">
    <header class="topbar">
      🚀 Rover Control System
    </header>

    <main>
      <router-view />
    </main>
  </div>
</template>

<style scoped>
.app {
  font-family: Arial, sans-serif;
}

.topbar {
  background: #111;
  color: white;
  padding: 10px 20px;
  font-size: 18px;
}

main {
  padding: 10px;
}
</style>
