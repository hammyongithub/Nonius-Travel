import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia'; // Import Pinia

const app = createApp(App);

const pinia = createPinia(); // Create Pinia store
app.use(pinia); // Use Pinia
// Vuetify
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import '@mdi/font/css/materialdesignicons.css';
import 'vuetify/dist/vuetify.min.css';

const vuetify = createVuetify({
  components,
  directives,
});

// Create a Pinia store and use it in your ap

app.use(router);
app.use(vuetify);

app.mount('#app');
