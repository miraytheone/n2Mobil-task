import './style.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App);

app.use(router);

const pinia = createPinia();

pinia.use(({ store }) => {
    store.$onAction(
      ({ storeName }) => {
        const state = store.state;
        localStorage.setItem(storeName, JSON.stringify(state));
      }
    );
  
    store.$subscribe(
      ({ storeName }) => {
        const savedState = localStorage.getItem(storeName);
        if (savedState) {
          store.state = JSON.parse(savedState);
        }
      }
    );
  });
  

app.use(pinia);

app.mount('#app');
