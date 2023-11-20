<template>
    <v-card>
      <v-card-title>{{ offer.hotel.name }}</v-card-title>
      <v-card-subtitle>{{ offer.hotel.chainCode }} - {{ offer.hotel.hotelID }} - Top Offer</v-card-subtitle>
      <v-card-text>
        Check-in Date: {{ offer.offers.checkInDate }}
        Check-out Date: {{ offer.offers.checkOutDate }}
        Description: {{ offer.offers.room.description.text }}
        Guests: Adults - {{ offer.offers.guests }}
        Price: {{ offer.offers.price.total }} {{ offer.offers.price.currency }}
        Cancelation: {{ offer.offers.policies.cancellations.deadline }}
        <!-- Display other hotel information here -->
      </v-card-text>
    </v-card>
  </template>
  
  <script>
  export default {
    props: {
      offer: Object, // The hotel object passed as a prop
    },
  };
  </script>
  