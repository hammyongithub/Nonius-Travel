<template>
  <v-card v-for="(offerItem, index) in offer.offers" :key="index">
    <v-card-title>{{ offer.hotel.name }}</v-card-title>
    <v-card-subtitle>{{ offer.hotel.chainCode }} - Top Offer</v-card-subtitle>
    <v-card-text>
      <p>Check-in Date: {{ offerItem.checkInDate }}</p>
      <p>Check-out Date: {{ offerItem.checkOutDate }}</p>
      <p>Room Type: {{ offerItem.room.type }}</p>
      <p>Description: {{ offerItem.room.description.text }}</p>
      <p>Beds: {{ offerItem.room.typeEstimated.beds }} {{ offerItem.room.typeEstimated.bedType }}</p>
      <p>Guests: {{ offerItem.guests.adults }} Adults</p>
      <p>Price: {{ offerItem.price.total }} {{ offerItem.price.currency }}</p>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    offer: Object, // The hotel offer object passed as a prop
  },
};
</script>
