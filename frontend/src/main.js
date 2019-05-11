import Vue from 'vue'
import App from './App.vue'

Vue.prototype.$BASE_URL = 'http://127.0.0.1:8000/api/v1/'

Vue.config.productionTip = false
Vue.use(require('vue-moment'))
new Vue({
  render: h => h(App)
}).$mount('#app')
