<template>
  <div>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12" sm="6" md="4">
          <v-text-field v-model="location" label="Location" outlined dense></v-text-field>
          <div>
            <v-date-picker></v-date-picker>
          </div>
        </v-col>
      </v-row>
      <v-btn @click="searchHotels" color="primary" dark>Search Hotels</v-btn>
    </v-container>
      <v-container>
      <v-row>
        <v-col cols="12" v-for="(hotel, index) in hotels.slice(0, 10)" :key="index">
          <hotel-card :hotel="hotel"></hotel-card>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
  </div>
</template>


<script>
import axios from 'axios'
import HotelCard from '@/components/HotelCard.vue'

export default {
  components: {
    HotelCard
  },
  data() {
    return {
      location: '',
      hotels: [],
    }
  },
  methods: {
    searchHotels() {
      axios
        .get('http://127.0.0.1:8000/api/v1/hotelsearch/', {
          params: {
            location: this.location,
          },
        })
        // .then((response) => {
        //   // Assuming the hotels array is inside a property named 'data' in the response object
        //   const hotelsArray = response.data.data;

        //   if (Array.isArray(hotelsArray)) {
        //     this.hotels = hotelsArray;
        //     console.log(this.hotels);
        //   } else {
        //     console.error('Invalid API response format: the "data" property is not an array');
        //     console.log(this.hotels);
        //   }
        // })
        .then((response) => {
          this.hotels = response.data.data;
          console.log(this.hotels);
        })
        .catch((error) => {
          console.error('Error fetching hotel data:', error);
        });
    },
  }
}
</script>