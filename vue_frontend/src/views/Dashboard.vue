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

export default {
  data() {
    return {
      latestclients: [],
    }
  },
  async mounted() {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/latestclients/')
      this.latestclients = response.data
      console.log(this.latestclients); // Add this line to check the data
    } catch (error) {
      console.error('Error fetching latest clients:', error)
    }
  }
}
</script>