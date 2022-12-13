import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

// set base url for backend
axios.defaults.baseURL = store.state.BASE_URL //'http://127.0.0.1:8000'

// если ошибка авторизации кидает на регистарция
// https://stackoverflow.com/questions/52096412/vue-js-and-axios-redirect-on-401
axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  console.log(error.response.data)
  if (error.response.status === 401) {
    // store.dispatch('logout')
    router.push({ name: 'LoginView'})
  }
  return Promise.reject(error)
})

import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap/dist/js/bootstrap.js'

const app = createApp(App).use(store).use(router).use(BootstrapVue3).mount('#app') //

export default app
