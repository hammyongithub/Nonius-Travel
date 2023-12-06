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
          @change="updateSettings"
        ></v-select>

        <!-- Currency Selector -->
        <v-select
          v-model="selectedCurrency"
          :items="currencies"
          label="Select Currency"
          @change="updateSettings"
        ></v-select>

        <!-- Time Zone Selector -->
        <v-select
          v-model="selectedTimeZone"
          :items="timezones"
          label="Select Time Zone"
          @change="updateSettings"
        ></v-select>
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" @click="updateSettings">Update Settings</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios';

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
      timezones: ['UTC', 'UTC+1', 'UTC+2', 'UTC+3', 'UTC+4', 'UTC+5', 'UTC+6', 'UTC+7', 'UTC+8', 'UTC+9', 'UTC+10', 'UTC+11', 'UTC+12'],
    };
  },
  mounted() {
    this.loadUserSettings();
  },
  methods: {
    loadUserSettings() {
      // Load the current user settings when the component is mounted
      const token = localStorage.getItem('authToken');
      if (token) {
        axios.get('http://127.0.0.1:8000/api/v1/auth/settings/', {
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
    updateSettings() {
      // Update the user settings
      const token = localStorage.getItem('authToken');
      if (token && this.selectedLanguage && this.selectedCurrency && this.selectedTimeZone) {
        axios.patch('http://127.0.0.1:8000/api/v1/auth/settings/', {
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
    }
  }
};
</script>
