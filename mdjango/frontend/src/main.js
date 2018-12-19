// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import Routes from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import qs from 'qs'
import echarts from 'echarts'
import 'echarts-wordcloud/dist/echarts-wordcloud.js'
import 'echarts-wordcloud/dist/echarts-wordcloud.min.js'

Vue.config.productionTip = false

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
Vue.prototype.$qs = qs
Vue.prototype.$echarts = echarts

Vue.use(ElementUI)
Vue.use(VueAxios, axios)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router: Routes,
  components: { App },
  template: '<App/>'
})
