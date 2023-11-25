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

    <div class="text-title-1 text-medium-emphasis d-flex align-center justify-space-between">Create an Account</div>

    <v-divider class="my-4"></v-divider>

    <v-text-field
      v-model="firstName"
      density="compact"
      placeholder="First Name"
      prepend-inner-icon="mdi-badge-account-outline"
      variant="outlined"
    ></v-text-field>

    <v-text-field
      v-model="lastName"
      density="compact"
      placeholder="Last Name"
      prepend-inner-icon="mdi-badge-account-outline"
      variant="outlined"
    ></v-text-field>

    <v-text-field
      v-model="email"
      density="compact"
      placeholder="Email address"
      prepend-inner-icon="mdi-email-outline"
      variant="outlined"
    ></v-text-field>
  
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
  
    <!-- Add additional registration fields as needed -->
  
    <v-btn
      block
      class="mb-8"
      color="blue"
      size="large"
      variant="tonal"
      @click="register"
    >Register</v-btn>
    </v-card>
  </div>
</template>
  
<script>
  export default {
    data: () => ({
      visible: false,
      firstName: '',
      lastName: '',
      email: '',
      password: '',
    }),
    methods: {
      register() {
        const userData = {
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          password: this.password,
        }
        axios
          .post('http://127.0.0.1:8000/api/v1/signup/', userData)
          .then((response) => {
            console.log(response.data);
          })
          .catch((error) => {
            
          })
      },
    },
  };
</script>
  