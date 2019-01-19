import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import routes from '../config/routes'
import api from './api/index.js'
import  fastClick from 'fastClick'
// 引用工具文件
import utils from './utils/index.js'

import { NoticeBar } from 'vant';
import { Tabbar, TabbarItem } from 'vant';
import { List,Cell } from 'vant';

Vue.use(List);
Vue.use(Cell);
Vue.use(Tabbar).use(TabbarItem);
Vue.use(NoticeBar);


Vue.config.productionTip = false
Vue.use(VueRouter)
fastClick.attach(document.body)
const router = new VueRouter({
  routes
})
// 将工具方法绑定到全局
Vue.prototype.$utils = utils
Vue.prototype.$api = api
Vue.config.productionTip = false
// 跑起来吧
new Vue({
  router,
  el: '#app',
  render: (h) => h(App)
})



