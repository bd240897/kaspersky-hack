import axios from "axios";
import router from '../../../router'

export default ({
    namespaced: true,
    state() {
        return {
            history: {},
        }
    },
    getters: {},
    mutations: {
        SET_HISTORY(state, history) {
            state.history = history.reverse()
        },
    },
    actions: {
        getHistory({commit, rootState}, {url = this.state.HISTORY_URL}) {
            axios.get(url)
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_HISTORY', x.data)
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

