<template>
  <div>
    <v-img
      class="mx-auto my-6"
      max-width="228"
      src="/src/assets/nonius.png"
    ></v-img>
 
    <v-card
      class="mx-auto pa-12 pb-8"
      elevation="1"
      max-width="448"
      rounded="lg"
    >
    <div class="text-subtitle-1 text-medium-emphasis">Account</div>

    <v-text-field
      v-model="email"
      density="compact"
      placeholder="Email"
      prepend-inner-icon="mdi-email-outline"
      variant="outlined"
    ></v-text-field>

    <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
      Password
    </div>

    <v-text-field
      v-model="password"
      :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
      :type="visible ? 'text' : 'password'"
      density="compact"
      placeholder="Enter your password"
      prepend-inner-icon="mdi-lock-outline"
      variant="outlined"
      @click:append-inner="visible = !visible"
    ></v-text-field>

    <v-card
      class="mb-12"
      color="surface-variant"
      variant="tonal"
    >
      <v-card-text class="text-medium-emphasis text-caption">
        Warning: After 3 consecutive failed login attempts, your account will be temporarily locked for three hours.
      </v-card-text>
    </v-card>

    <v-btn
      block
      class="mb-8"
      color="blue"
      size="large"
      variant="tonal"
      @click="login"
    >Log In</v-btn>
  </v-card>
</div>
</template>
  
<script>
import { ref } from 'vue';
import { useStore } from '../store.js'; // Adjust the path to your store file
import axios from 'axios';
import router from '../router';
import { apiUrl } from "../apiconfig.js"

export default {
  setup() {
    const email = ref('');
    const password = ref('');
    const visible = ref(false);
    const authStore = useStore(); // Use the store
    const baseUrl = process.env.VUE_APP_API_BASE_URL;

    const login = async () => {
      try {
        const response = await axios.post('https://evening-coast-93489-45f54e292976.herokuapp.com/api/v1/auth/token/login', {
          email: email.value,
          password: password.value,
        });
        const token = response.data.auth_token;
        console.log(token);
        localStorage.setItem('authToken', token);
        authStore.login(); // Call the store action to set the user as logged in
        axios.defaults.headers.common['Authorization'] = `Token ${token}`;
        // Redirect to the home page
        router.push({ name: 'home' }); // Replace 'HomePage' with the name of the route you want to redirect to
      } catch (error) {
        console.error(error);
        alert('Login failed. Please check your username and password.');
      }
    };

    return {
      email,
      password,
      visible,
      login, //rebuild lmao
    };
  },
};
</script>
