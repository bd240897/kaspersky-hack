import axios from "axios";
import router from '../../../router'

export default ({
    namespaced: true,
    state() {
        return {}
    },
    getters: {},
    mutations: {},
    actions: {
        REGISTER({commit, rootState, dispatch}, {url = this.state.REGISTER_URL, data = {"login": '', "password": ''}}) {
            return axios.post(url, data)
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    // commit('SET_ERROR', x.data.auth_token)
                    // dispatch("getUserInfo", {})
                    router.push({name: 'CreateProfileView'})
                    return x
                })
        },
    },


})

