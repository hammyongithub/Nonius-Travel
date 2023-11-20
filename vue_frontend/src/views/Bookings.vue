<!-- <v-container>
  <v-row>
    <v-col cols="12" v-for="(hotel, index) in hotels.slice(0, 10)" :key="index">
      <hotel-card :hotel="hotel"></hotel-card>
    </v-col>
  </v-row>
</v-container> -->

<template>
  <div>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12" sm="6" md="4">
          <v-text-field v-model="location" label="Location" outlined dense></v-text-field>
          <v-text-field v-model="checkInDate" label="Check-in Date" type="date" outlined dense></v-text-field>
          <v-text-field v-model="checkOutDate" label="Check-out Date" type="date" outlined dense></v-text-field>
          <v-text-field v-model="adults" label="Guests" type="number" outlined dense></v-text-field>
          <v-text-field v-model="roomQuantity" label="Rooms" type="number" outlined dense></v-text-field>
          <v-text-field v-model="priceMin" label="Minimum Price" type="number" outlined dense></v-text-field>
          <v-text-field v-model="priceMax" label="Maximum Price" type="number" outlined dense></v-text-field>
          <v-text-field v-model="currency" label="Currency" outlined dense></v-text-field>
          <v-text-field v-model="boardType" label="Board Type" outlined dense></v-text-field>
        </v-col>
      </v-row>
      <v-btn @click="searchHotels" color="primary" dark>Search Hotels</v-btn>
      <v-btn @click="searchOffers" color="primary" dark>Search Offers</v-btn>
    </v-container>
    <v-container>
      <v-row>
        <v-col cols="12" v-for="(offer, index) in hotelOffers" :key="index">
          <hotel-card :offer="offer"></hotel-card>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
  </div>
</template>


<script>
import axios from 'axios'
import HotelCard from '../components/HotelCard.vue'

export default {
  components: {
    HotelCard,
  },
  data() {
    return {
      location: '',
      hotels: [],
      hotelIds: [],
      checkInDate: '',
      checkOutDate: '',
      adults: '',
      roomQuantity: '',
      priceMin: '',
      priceMax: '',
      currency: '',
      boardType: '',
      hotelOffers: [],
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
        .then((response) => {
          console.log(response.data.data);
          this.hotels = response.data.data;
          console.log(this.hotels);
          for (let i = 0; i < 50; i++) {
            this.hotelIds.push(response.data.data[i].hotelId);
          }
          console.log(this.hotelIds);
        })
        .catch((error) => {
          console.error('Error fetching hotel data:', error);
        });
    },
    searchOffers() {
    const hotelIdsString = JSON.stringify(this.hotelIds);

    axios
        .get('http://127.0.0.1:8000/api/v1/offersearch/', {
            params: {
                hotelIds: hotelIdsString,
                // adults: this.adults,
                // checkInDate: this.checkInDate,
                // checkOutDate: this.checkOutDate,
                // roomQuantity: this.roomQuantity,
                // priceRange: this.priceMin.toString() + '-' + this.priceMax.toString(),
                // currency: this.currency,
                // boardType: this.boardType,
            },
        })
        .then((response) => {  
          this.hotelOffers = response.data.data;
          console.log(this.hotelOffers);

        })
        .catch((error) => {
            console.error('Error fetching hotel offers:', error);
        });
    },
  }
}
</script>