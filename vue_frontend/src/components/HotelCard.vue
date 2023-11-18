<template>
    <v-card>
      <v-card-title>{{ hotel.name }}</v-card-title>
      <v-card-subtitle>{{ hotel.chainCode }}</v-card-subtitle>
      <v-card-text>
        <!-- Display other hotel information here, next is date -->
      </v-card-text>
    </v-card>
  </template>
  
  <script>
  export default {
    props: {
      hotel: Object, // The hotel object passed as a prop
    },
  };
  </script>
  