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

        <v-combobox
          v-model="selectedTimeZone"
          :items="timezones"
          label="Select Time Zone"
        ></v-combobox>
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" @click="updateSettings">Update Settings</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios';
import moment from 'moment-timezone';

export default {
  data() {
    return {
      selectedLanguage: '',
      selectedCurrency: '',
      selectedTimeZone: '',
      languages: [
        'English',
        'Spanish',
      ],
      currencies: ['USD', 'EUR', 'GBP', 'JPY', 'CNY'],
      timezones: [],
    };
  },
  mounted() {
    this.loadUserSettings();
    this.loadTimeZones();
  },
  methods: {
    loadUserSettings() {
      // Load the current user settings when the component is mounted
      const token = localStorage.getItem('authToken');
      if (token) {
        axios.get('https://evening-coast-93489-45f54e292976.herokuapp.com/api/v1/auth/settings/', {
          headers: {
            Authorization: `Token ${token}`
          }
        }).then(response => {
          this.selectedLanguage = response.data.user_language;
          this.selectedCurrency = response.data.user_currency;
          this.selectedTimeZone = response.data.user_timezone;
        }).catch(error => {
          console.error(error);
        });
      }
    },
    loadTimeZones() {
    // Load timezone options from moment-timezone
    this.timezones = moment.tz.names();
    },
    updateSettings() {
      // Update the user settings
      const token = localStorage.getItem('authToken');
      if (token && this.selectedLanguage && this.selectedCurrency && this.selectedTimeZone) {
        axios.patch('https://evening-coast-93489-45f54e292976.herokuapp.com/api/v1/auth/settings/', {
          user_language: this.selectedLanguage,
          user_currency: this.selectedCurrency,
          user_timezone: this.selectedTimeZone
        }, {
          headers: {
            Authorization: `Token ${token}`
          }
        }).then(response => {
          alert('Settings updated successfully!');
        }).catch(error => {
          console.error(error);
          alert('Failed to update settings. Please try again.');
        });
      }
    },
  }
};
</script>
