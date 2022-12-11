import axios from "axios";
import router from '../../../router'

export default ({
    namespaced: true,
    state() {
        return {
            TOKEN: "",
            userInfo: {},
        }
    },
    getters: {},
    mutations: {
        SET_TOKEN(state, TOKEN) {
            state.TOKEN = TOKEN
            axios.defaults.headers.common['Authorization'] = 'Token ' + TOKEN;
        },
        SET_USER_INFO(state, userInfo) {
            state.userInfo = userInfo
        },
    },
    actions: {
        IS_PROFILE_EXISTS({commit, rootState}, {url = this.state.PROFILE_URL,}) {
            // проверяет существование профиля и направляет либо на создание либо в профиль
            axios.get(url)
                .then(function (x) {
                    console.log(x.data)
                    console.log('Profile exists!!');
                    router.push({ name: 'ProfileView'})
                })
                .catch(err => {
                    console.log(err)
                    if (err.response) {
                        console.log("client received an error response (5xx, 4xx)")
                        console.log('Profile doesn\'t exist!!');
                        router.push({ name: 'CreateProfileView'})
                    } else if (err.request) {
                        console.log("client never received a response, or request never left")
                    } else {
                        console.log("anything else ")
                    }
                    return err
                })
        },

        LOGIN({commit, rootState, dispatch}, {url = this.state.LOGIN_URL, data = {"login": '', "password": ''}}) {
            axios.post(url, data)
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_TOKEN', x.data.auth_token)
                    dispatch("IS_PROFILE_EXISTS", {})
                })
                .catch(err => {
                    console.log(err)
                    if (err.response) {
                        console.log("client received an error response (5xx, 4xx)")
                    } else if (err.request) {
                        console.log("client never received a response, or request never left")
                    } else {
                        console.log("anything else ")
                    }
                    return err
                })
        },

        getUserInfo({commit, rootState}, {url = this.state.USER_INFO_URL}) {
            axios.get(url)
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_USER_INFO', x.data)
                })
                .catch(err => {
                    console.log(err)
                    if (err.response) {
                        console.log("client received an error response (5xx, 4xx)")
                    } else if (err.request) {
                        console.log("client never received a response, or request never left")
                    } else {
                        console.log("anything else ")
                    }
                    return err
                })
        },
    },


})

