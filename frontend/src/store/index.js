import { createStore } from 'vuex'
import login from "./modules/login/";
import register from "./modules/register/";
import profile from "./modules/profile/";
import quick_start from "./modules/quick_start/";
export default createStore({
  state() {
    return {
      // TODO
      BASE_URL: 'http://51.250.76.141:8000', //'http://127.0.0.1:8000',
      REGISTER_URL: "/api/v1/auth/users/",
      LOGIN_URL: "/auth/token/login",

      USER_INFO_URL: "/api/v1/auth/users/me/",


      PROFILE_URL: "/api/v2/profile/",
      QUICK_START_URL: "api/v2/request/photo/quick/",

      WALLETS_LIST_URL: "/api/v1/wallet/list/",
      WallET_URL: "api/v1/wallet/",
      MAKE_TRANSFER_URL: "api/v1/transfer/",
      HISTORY_URL: "api/v1/transfer/history/",

      CHAT_HISTORY_URL: "/chat/history",
      CHAT_SEND_URL: "/message/send",
      CHAT_ID_DIALOG_URL: '/chat/dialog',
      IS_TOKEN_VALID_URL: "/jwt/verify",
      SEND_MSG_URL: "/message/send"
      // IS_TOKEN_VALID_URL_full: "https://hack.invest-open.ru/jwt/verify"
    }
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    login,
    register,
    profile,
    quick_start,
  }
})
