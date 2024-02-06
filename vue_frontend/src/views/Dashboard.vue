<template>
  <div id="app">
  <v-container>
    <v-grid>
      <v-row>
        <v-col cols="auto">
          <h1 class="text-h4 text--primary" style="text-align: center">Latest Clients</h1>
        </v-col>
      </v-row>
      <v-row v-if="latestclients.length > 0">
        <v-col cols="auto">
          <v-card>
            <v-card-title primary-title>
              {{ latestclients[0].name }}
            </v-card-title>
            <v-card-subtitle>
              {{ latestclients[0].client_contact[0].email }}  |  {{ latestclients[0].client_contact[0].phone }}
            </v-card-subtitle>
            <v-card-text>
              
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="auto">
          <v-card>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="auto">
          <v-card>
          </v-card>
        </v-col>
        <v-col cols="auto">
          <v-card>
          </v-card>
        </v-col>
      </v-row>
    </v-grid>
  </v-container>
  </div>
</template>


<script>
import axios from 'axios'
import { apiUrl } from "../apiconfig.js"

export default {
  data() {
    return {
      latestclients: [],
    }
  },
  async mounted() {
    const baseUrl = process.env.VUE_APP_API_BASE_URL; // Access the environment variable

    try {
      const response = await axios.get(`${apiUrl}latestclients`) // Use template literals to insert the variable
      this.latestclients = response.data
      console.log(this.latestclients); // This will help you to see the fetched data in the console
    } catch (error) {
      console.error('Error fetching latest clients:', error)
    }
  }
}
</script>