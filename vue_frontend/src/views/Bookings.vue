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
            <v-select v-model="currency" label="Currency"  :items="currencyList" outlined dense></v-select>
          </v-col>
          <v-col cols="12" sm="6">
            <v-select v-model="boardType" label="Board Type"  :items="boardTypeList" outlined dense></v-select>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col cols="12">
            <v-btn
              @click="searchHotelsAndOffers"
              :disabled="!canSearch"
              color="primary"
              dark
            >Search Hotels and Offers</v-btn>
          </v-col>
        </v-row>

        <v-row v-if="loading">
          <v-col class="text-center">
            <v-progress-circular indeterminate color="primary"></v-progress-circular>
          </v-col>
        </v-row>
        <!-- Displaying hotel offers -->
        <v-row v-else>
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
import { apiUrl } from "../apiconfig.js"

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
      boardTypeList: ["ROOM_ONLY", "BREAKFAST"],
      currencyList: ["EUR", "USD", "GBP", "JPY", "CNY"],
    }
  },
  mounted() {
    this.userCurrencyLoader();
    this.setDefaultDates();
  },
  computed: {
    iataCodes() {
      return this.iataJSON.map((airport) => `${airport.iata} - ${airport.country} - ${airport.city}`);
    },
    canSearch() {
      return this.location && this.checkInDate && this.checkOutDate && this.adults && this.roomQuantity;
    },
  },

  methods: {
    async searchHotelsAndOffers() {
      if (this.location) {
        this.loading = true; // Start loading
        try {
          await this.searchHotels(); // Wait for searchHotels to complete
          await this.searchOffers(); // Then execute searchOffers
        } catch (error) {
          console.error('Error in hotel and offer search:', error);
        }
      }
    },
    async searchHotels() {
      const locationCode = this.location.substring(0, 3);
      try {
        const response = await axios.get(`${apiUrl}hotelsearch/`, {
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
      axios
        .get(`${apiUrl}offersearch/`, { params })
        .then((response) => {
          this.hotelOffers = response.data.data;
          console.log(this.hotelOffers);
          this.loading = false;
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
    userCurrencyLoader() {
      const token = localStorage.getItem('authToken');
      if (token) {
        axios.get(`${apiUrl}auth/settings/`, {
          headers: {
            Authorization: `Token ${token}`
          }
        }).then(response => {
          this.currency = response.data.user_currency;
        }).catch(error => {
          console.error(error);
        });
      }
    },
    setDefaultDates() {
      const today = new Date();
      const tomorrow = new Date(today);
      tomorrow.setDate(tomorrow.getDate() + 1);

      const weekAfterTomorrow = new Date(tomorrow);
      weekAfterTomorrow.setDate(weekAfterTomorrow.getDate() + 6);

      // Format the dates to YYYY-MM-DD for the date input fields
      this.checkInDate = this.formatDate(tomorrow);
      this.checkOutDate = this.formatDate(weekAfterTomorrow);
    },
    formatDate(date) {
      let month = '' + (date.getMonth() + 1),
          day = '' + date.getDate(),
          year = date.getFullYear();

      if (month.length < 2) 
          month = '0' + month;
      if (day.length < 2) 
          day = '0' + day;

      return [year, month, day].join('-');
    }
  }
}
</script>