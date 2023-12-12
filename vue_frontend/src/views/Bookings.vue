<template>
  <div>
    <v-form>
      <v-container>
        <!-- Inputs for hotel search -->
        <v-row>
          <v-col cols="12" sm="6">
            <v-combobox
              v-model="location"
              :items="iataCodes"
              :filter="filterSearch"
              label="Location"
              item-text="label"
              item-value="value"
              clearable
              outlined
              dense
            ></v-combobox>
          </v-col>
          <v-col cols="12" sm="3">
            <v-text-field type="date" v-model="checkInDate" label="Check-in Date" outlined dense></v-text-field>
          </v-col>
          <v-col cols="12" sm="3">
            <v-text-field type="date" v-model="checkOutDate" label="Check-out Date" outlined dense></v-text-field>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col cols="12" sm="6">
            <v-text-field type="number" v-model="adults" label="Guests" outlined dense></v-text-field>
          </v-col>
          <v-col cols="12" sm="6">
            <v-text-field type="number" v-model="roomQuantity" label="Rooms" outlined dense></v-text-field>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col cols="12" sm="6">
            <v-text-field type="number" v-model="priceMin" label="Minimum Price" outlined dense></v-text-field>
          </v-col>
          <v-col cols="12" sm="6">
            <v-text-field type="number" v-model="priceMax" label="Maximum Price" outlined dense></v-text-field>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col cols="12" sm="6">
            <v-text-field v-model="currency" label="Currency" outlined dense></v-text-field>
          </v-col>
          <v-col cols="12" sm="6">
            <v-text-field v-model="boardType" label="Board Type" outlined dense></v-text-field>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col cols="12">
            <v-btn
              @click="searchHotelsAndOffers"
              :disabled="!location"
              color="primary"
              dark
            >Search Hotels and Offers</v-btn>
          </v-col>
        </v-row>

        <v-overlay :value="loading">
          <v-progress-circular indeterminate color="primary"></v-progress-circular>
        </v-overlay>

        <!-- Displaying hotel offers -->
        <v-row>
          <v-col cols="12" v-for="(offer, index) in hotelOffers.slice(0, 9)" :key="index">
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
import airports from '../assets/airports.json'

export default {
  components: {
    HotelCard,
  },
  data() {
    return {
      iataJSON: airports,
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
      loading: false,
    }
  },
  computed: {
    iataCodes() {
      return this.iataJSON.map((airport) => `${airport.iata} - ${airport.country} - ${airport.city}`);
    },
  },

  methods: {
    async searchHotelsAndOffers() {
      if (this.location) {
        this.loading = true;
        try {
          await Promise.all([this.searchHotels(), this.searchOffers()]);
        } catch (error) {
          console.error('Error in fetching data:', error);
        } finally {
          this.loading = false;
        }
      }
    },
    async searchHotels() {
      const locationCode = this.location.substring(0, 3);
      const baseUrl = process.env.VUE_APP_API_BASE_URL;
      try {
        const response = await axios.get('https://evening-coast-93489-45f54e292976.herokuapp.com/api/v1/hotelsearch/', {
          params: { location: locationCode },
        });
        this.hotels = response.data.data.slice(0, 19); // Dont forget to change this, limit only 20 for testing
        this.hotelIds = this.hotels.map(hotel => hotel.hotelId);
      } catch (error) {
        console.error('Error fetching hotel data:', error);
      }
    },
    searchOffers() {
      const params = {};
      const baseUrl = process.env.VUE_APP_API_BASE_URL;
      // Add each parameter only if it is not empty
      if (this.hotelIds.length > 0) {
        params.hotelIds = JSON.stringify(this.hotelIds);
      }
      if (this.adults) {
        params.adults = this.adults;
      }
      if (this.checkInDate) {
        params.checkInDate = this.checkInDate;
      }
      if (this.checkOutDate) {
        params.checkOutDate = this.checkOutDate;
      }
      if (this.roomQuantity) {
        params.roomQuantity = this.roomQuantity;
      }
      if (this.priceMin) {
        params.priceMin = this.priceMin;
      }
      if (this.priceMax) {
        params.priceMax = this.priceMax;
      }
      if (this.currency) {
        params.currency = this.currency;
      }
      if (this.boardType) {
        params.boardType = this.boardType;
      }

      // Make the request with only the non-empty parameters
      return axios
        .get('https://evening-coast-93489-45f54e292976.herokuapp.com/api/v1/offersearch/', { params })
        .then((response) => {
          this.hotelOffers = response.data.data;
          console.log(this.hotelOffers);
        })
        .catch((error) => {
          console.error('Error fetching hotel offers:', error);
        });
    },
    filterSearch(item, queryText, itemText) {
      const text = item.label.toLowerCase();
      const searchText = queryText.toLowerCase();

      return text.indexOf(searchText) > -1;
    },
  }
}
</script>