<template>
    <div id="app">
      <v-container>
        <v-grid>
          <v-row>
            <v-col cols="12">
              <h1 style="text-align: center" class="text-h4 text--primary">Nonius Travel Booking Interface</h1>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="6">
              <v-card image="src/assets/wave.jpg" to="/dashboard">
                <v-card-title primary-title>
                    <h3 class="text-h6 mb-1">DashBoard</h3>
                  </v-card-title>
                    <v-list lines="3">
                      <v-list-item class="text-caption">Overview of sales figures</v-list-item>
                      <v-list-item class="text-caption">Top-selling destinations</v-list-item>
                      <v-list-item class="text-caption">Recent bookings</v-list-item>
                    </v-list>
              </v-card>
            </v-col>
            <v-col cols="6">
              <v-card image="src/assets/wave.jpg" to="/customers">
                <v-card-title primary-title>
                    <h3 class="text-h6 mb-1">Customer Management</h3>
                  </v-card-title>
                    <v-list lines="3">
                      <v-list-item class="text-caption">Customer profiles with contact information and booking history</v-list-item>
                      <v-list-item class="text-caption">CRM tools for marketing, reminders, and feedbacks</v-list-item>
                      <v-list-item class="text-caption"></v-list-item>
                    </v-list>
              </v-card>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="6">
              <v-card image="src/assets/wave.jpg" to="/bookings">
                <v-card-title primary-title>
                    <h3 class="text-h6 mb-1">Booking Management</h3>
                  </v-card-title>
                    <v-list lines="3">
                      <v-list-item class="text-caption">Create, update, and cancel bookings</v-list-item>
                      <v-list-item class="text-caption">Manage individual and group bookings</v-list-item>
                      <v-list-item class="text-caption">View real-time booking status</v-list-item>
                    </v-list>
              </v-card>
            </v-col>
            <v-col cols="6">
              <v-card image="src/assets/wave.jpg" to="/packages">
                <v-card-title primary-title>
                    <h3 class="text-h6 mb-1">Package and Itinerary Management</h3>
                  </v-card-title>
                    <v-list lines="3">
                      <v-list-item class="text-caption">Add, edit, or delete tour packages</v-list-item>
                      <v-list-item class="text-caption">Define itineraries with details on destinations, accommodations, and activities</v-list-item>
                      <v-list-item class="text-caption"></v-list-item>
                    </v-list>
              </v-card>
            </v-col>
          </v-row>
        </v-grid>
      </v-container>
    </div>
  </template>

<script>
export default {

}
</script>

<style>

</style>
