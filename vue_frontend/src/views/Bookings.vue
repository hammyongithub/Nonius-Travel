<template>
  <div>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12" sm="6" md="4">
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
          <v-text-field type="date" v-model="checkInDate" label="Check-in Date" outlined dense></v-text-field>
          <v-text-field type="date" v-model="checkOutDate" label="Check-out Date" outlined dense></v-text-field>
          <v-text-field type="number" v-model="adults" label="Guests" outlined dense></v-text-field>
          <v-text-field type="number" v-model="roomQuantity" label="Rooms" outlined dense></v-text-field>
          <v-text-field type="number" v-model="priceMin" label="Minimum Price" outlined dense></v-text-field>
          <v-text-field type="number" v-model="priceMax" label="Maximum Price" outlined dense></v-text-field>
          <v-text-field v-model="currency" label="Currency" outlined dense></v-text-field>
          <v-text-field v-model="boardType" label="Board Type" outlined dense></v-text-field>
        </v-col>
      </v-row>
      <v-btn @click="searchHotels" color="primary" dark>Search Hotels</v-btn>
      <v-btn @click="searchOffers" color="primary" dark>Search Offers</v-btn>
      <v-btn @click="print" color="primary" dark>prints</v-btn>
    </v-container>
    <v-container>
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
    }
  },
  computed: {
    iataCodes() {
      return this.iataJSON.map((airport) => `${airport.iata} - ${airport.country} - ${airport.city}`);
    },
  },

  methods: {
    searchHotels() {
      const locationCode = this.location.substring(0, 3);
      axios
        .get('http://127.0.0.1:8000/api/v1/hotelsearch/', {
          params: {
            location: locationCode,
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
                adults: this.adults,
                checkInDate: this.checkInDate,
                checkOutDate: this.checkOutDate,
                roomQuantity: this.roomQuantity,
                priceRange: this.priceMin.toString() + '-' + this.priceMax.toString(),
                currency: this.currency,
                boardType: this.boardType,
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
    filterSearch(item, queryText, itemText) {
      const text = item.label.toLowerCase();
      const searchText = queryText.toLowerCase();

      return text.indexOf(searchText) > -1;
    },
    print() {
      console.log(this.location)
    }
  }
}
</script>