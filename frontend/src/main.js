import Vue from 'vue'
import App from './App.vue'
//import store from './store.js';
import VueMaterial from 'vue-material';
import HighchartsVue from "highcharts-vue";
import 'vue-material/dist/vue-material.css'
import 'vue-material/dist/theme/default.css'
import axios from 'axios'
import VueAxios from 'vue-axios'



Vue.config.productionTip = false

Vue.use(VueMaterial)
Vue.use(HighchartsVue);
Vue.use(VueAxios, axios)



new Vue({
  //store,
  render: h => h(App),
}).$mount('#app')
