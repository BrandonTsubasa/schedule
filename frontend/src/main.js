import Vue from "vue";
import App from "./App.vue";
import axios from "axios"
import router from "./router/index";
import vuetify from "vuetify";

import {
  ValidationProvider,
  ValidationObserver,
  extend,
  localize,
  setInteractionMode
} from 'vee-validate';
import ja from 'vee-validate/dist/locale/ja.json';
import { required, email, confirmed, min, max } from 'vee-validate/dist/rules';


// 必要なルールのみインポート
extend('required', required);
extend('email', email);
extend('confirmed', confirmed);
extend('min', min);
extend('max', max);


// メッセージを設定
localize('ja', ja);

// インタラクションモードをセット(グローバルで適用)
setInteractionMode('eager');

Vue.config.productionTip = false;
Vue.prototype.$axios = axios
Vue.use(vuetify);
Vue.use(axios);

Vue.component("ValidationProvider", ValidationProvider);
Vue.component("ValidationObserver", ValidationObserver);


axios.defaults.baseURL = "http://localhost:8000";
axios.defaults.headers.common["Accept"] = "application/json";
axios.defaults.headers.common["Content-Type"] = "application/json;charset=utf-8";
axios.defaults.headers.common["Access-Control-Allow-Origin"] = "http://localhost:8000";
axios.defaults.headers.common["X-Requested-With"] = "XMLHttpRequest";



new Vue({
  router,
  vuetify: new vuetify(),
  render: (h) => h(App)
}).$mount("#app");
