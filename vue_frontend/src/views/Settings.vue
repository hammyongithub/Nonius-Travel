<template>
    <v-container>
      <v-card>
        <v-card-title>Settings</v-card-title>
        <v-card-text>
          <!-- Language Selector -->
          <v-select
            v-model="selectedLanguage"
            :items="languages"
            label="Select Language"
          ></v-select>
  
          <!-- Currency Selector -->
          <v-select
            v-model="selectedCurrency"
            :items="currencies"
            label="Select Currency"
          ></v-select>

          <!-- Time Zone Selector -->
          <v-select
            v-model="selectedTimeZone"
            :items="timezones"
            label="Select Time Zone"
          ></v-select>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedLanguage: null,
        selectedCurrency: null,
        languages: [
          'English',
          'Spanish',
        ],
        currencies: ['USD', 'EUR', 'GBP', 'JPY', 'CNY'],
        timezones: ['UTC', 'UTC+1', 'UTC+2', 'UTC+3', 'UTC+4', 'UTC+5', 'UTC+6', 'UTC+7', 'UTC+8', 'UTC+9', 'UTC+10', 'UTC+11', 'UTC+12'],
      };
    },
  };
  </script>
  