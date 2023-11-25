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
        placeholder="Email address"
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
          Warning: After 3 consecutive failed login attempts, you account will be temporarily locked for three hours.
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
  import axios from 'axios';

  export default {
    data: () => ({
      visible: false,
      email: '',
      password: '',
    }),
    methods: {
      login() {
        const userData = {
          email: this.email,
          password: this.password,
        };
      axios
        .post('http://127.0.0.1:8000/api/v1/login/', userData)
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.error(error);
        });
      }
    }
  }
</script>