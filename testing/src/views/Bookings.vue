<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12" sm="6" md="4">
          <v-text-field v-model="location" label="Location" outlined dense></v-text-field>
        </v-col>
      </v-row>
      <v-btn @click="searchHotels" color="primary" dark>Search Hotels</v-btn>
    </v-container>
  </v-form>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      location: '',
      hotels: [],
    }
  },
  methods: {
    searchHotels() {
      axios.get('http://127.0.0.1:8000/api/v1/hotelsearch/', {
        params: {
          location: this.location,
        },
      })
      .then(response => {
        this.hotels = response.data; // Update your data to display search results
        console.log(this.hotels);
      })
      .catch(error => {
        console.error('Error fetching hotel data:', error);
      });
    },
  }
}
</script>