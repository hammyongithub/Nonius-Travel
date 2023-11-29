<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :rail="rail"
      permanent
      @click="rail = false"
    >

    <v-list density="compact" nav>
      <v-list-item
        to="/home"
        prepend-icon="mdi-home"
        title="Nonius Travel"
        nav 
      >
        <template v-slot:append>
        <v-btn
            variant="text"
            icon="mdi-chevron-left"
            @click.stop.prevent="rail = !rail"
          ></v-btn>
        </template>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

      <v-list density="compact" nav>
        <v-list-item prepend-icon="mdi-monitor-dashboard" title="Dashboard" value="dashboard" to="/dashboard"></v-list-item>
        <v-list-item prepend-icon="mdi-account-box-multiple-outline" title="Customer Management" value="customers" to="/customers"></v-list-item>
        <v-list-item prepend-icon="mdi-bed" title="Booking Management" value="booking" to="/bookings"></v-list-item>
        <v-list-item prepend-icon="mdi-map-legend" title="Packages and Itineraries" value="packages" to="/packages"></v-list-item>
        <v-list-item prepend-icon="mdi-cog" title="Settings" value="settings" height="10%" to="/settings"></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-toolbar density="compact">
      
      <v-spacer></v-spacer>

      <v-btn
        icon
        :color="theme.global.name.value ? 'light' : 'dark'"
        @click="toggleTheme"
      >
        <v-icon>mdi-theme-light-dark</v-icon>
      </v-btn>

      <v-btn v-if="isLoggedIn !== null && isLoggedIn" color="primary" variant="text" @click="logout">
        Logout
      </v-btn>
      <v-btn v-else color="primary" variant="text" to="/login">
        Login
      </v-btn>

    </v-toolbar>
  
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>

<script>
import { useStore } from './store.js';
import { useTheme } from 'vuetify/lib/framework.mjs';
import { computed } from 'vue';
import router from './router'; // Import your router instance

export default {
  beforeRouteUpdate(to, from, next) {
    // Trigger the setup function when the route is updated
    this.setup();
    next();
  },

  setup() {
    const theme = useTheme();
    function toggleTheme() {
      theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark';
    }

    const authStore = useStore();
    const logout = () => {
      authStore.logout();
      router.push({ name: 'login' });
    };

    console.log(authStore.isLoggedIn);

    return {
      isLoggedIn: computed(() => authStore.isLoggedIn), // Use computed to ensure reactivity
      logout,
      toggleTheme,
      theme,
    };
  },

  data() {
    return {
      drawer: true,
      rail: true,
    };
  },
};
</script>