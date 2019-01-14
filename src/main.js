import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import routes from '../config/routes'
import api from './api/index.js'
Vue.config.productionTip = false
Vue.use(VueRouter)
const router = new VueRouter({
  routes
})

Vue.prototype.$api = api
Vue.config.productionTip = false
// 跑起来吧
new Vue({
  router,
  el: '#app',
  render: (h) => h(App)
})

