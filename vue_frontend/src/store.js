    import { defineStore } from 'pinia';

    // Define your Pinia store
    export const useStore = defineStore('store', {
    state: () => ({
        isLoggedIn: false,
    }),
    actions: {
        login() {
        this.isLoggedIn = true;
        },
        logout() {
        this.isLoggedIn = false;
        },
    },
    });
