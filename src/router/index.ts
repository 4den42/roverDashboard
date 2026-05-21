import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: dashBoardView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
