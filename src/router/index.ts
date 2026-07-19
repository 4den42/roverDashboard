import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/dashBoardView.vue'
import LoginView from '../views/LoginView.vue'
import { useAuthStore } from '../stores/auth'

const routes = [
  { path: '/', name: 'dashboard', component: DashboardView },
  { path: '/login', name: 'login', component: LoginView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach(async (to) => {
  if (to.name === 'login') return true
  const auth = useAuthStore()
  if (!auth.checked) await auth.check()
  if (!auth.authenticated) return { name: 'login' }
  return true
})

export default router
