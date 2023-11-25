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

      <v-btn
        to="/login"
        variant="text"
        text="login">
      </v-btn>

      <v-btn
        to="/signup"
        variant="text"
        text="signup">
      </v-btn>
    
    </v-toolbar>
  
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>

<script>
  export default {
    data () {
      return {
        drawer: true,
        rail: true,
      }
    },
    methods: {

    },
    components: {
      
    }
  }
</script>

<script setup>
  import { useTheme } from 'vuetify/lib/framework.mjs';

  const theme=useTheme()

  function toggleTheme () {
    theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
  }
</script>