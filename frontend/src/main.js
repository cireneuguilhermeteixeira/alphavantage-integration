import Vue from 'vue'
import App from './App.vue'
import store from './store.js';
import VueMaterial from 'vue-material';
import HighchartsVue from "highcharts-vue";
import 'vue-material/dist/vue-material.css'
import 'vue-material/dist/theme/default.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-toast-notification/dist/theme-default.css';
import axios from 'axios'
import VueAxios from 'vue-axios'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueToast from 'vue-toast-notification';
// Import one of available themes


Vue.config.productionTip = false

Vue.use(VueMaterial)
Vue.use(HighchartsVue);
Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueToast,{ position: 'top'});

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
