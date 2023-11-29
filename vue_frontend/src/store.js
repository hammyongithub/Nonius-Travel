import { defineStore } from 'pinia';

// Define your Pinia store
export const useStore = defineStore('store', {
  state: () => ({
    isLoggedIn: false,
  }),
  actions: {
    login() {
      // Perform login logic here.
      // After a successful login, update the login state.
      this.isLoggedIn = true;
    },
    logout() {
      // Perform logout logic here.
      // After a successful logout, update the login state.
      this.isLoggedIn = false;
    },
  },
});
