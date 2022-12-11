import axios from "axios";
import router from '../../../router'

export default ({
    namespaced: true,
    state() {
        return {
            diseases: [],
        }
    },
    getters: {},
    mutations: {
        SET_DISEASES(state, diseases) {
            state.diseases = diseases
        },
    },
    actions: {
        SEND_PHOTO({commit, rootState}, {url = this.state.QUICK_START_URL, formData}) {
            return axios.post(url, formData, {headers: {'Content-Type': 'multipart/form-data'}})
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_DISEASES', x.data)
                    router.push({ name: 'ResultView'})
                    return x
                })
        },

    },


})

