import { createRouter, createWebHistory } from 'vue-router';
import { useStore } from '../store'; // Adjust the path to your Pinia store as needed
import HomeView from '../views/HomeView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'entry',
      component: HomeView
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('../views/Settings.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/Dashboard.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/customers',
      name: 'customers',
      component: () => import('../views/Customers.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/bookings',
      name: 'bookings',
      component: () => import('../views/Bookings.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/packages',
      name: 'packages',
      component: () => import('../views/Packages.vue'),
      meta: { requiresAuth: true }
    },
    // ... any other routes
  ]
});

router.beforeEach((to, from, next) => {
  const store = useStore(); // Use your Pinia store

  // Check if the route requires authentication
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

  if (requiresAuth && !store.isLoggedIn) {
    // If the user is not logged in, redirect to the login page
    next({ name: 'login' });
  } else {
    // Otherwise, proceed as normal
    next();
  }
});

export default router;
