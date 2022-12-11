import axios from "axios";
import router from '../../../router'

export default ({
    namespaced: true,
    state() {
        return {
            wallet_info: {},
        }
    },
    getters: {},
    mutations: {
        SET_WALLET_INFO(state, wallet_info) {
            state.wallet_info = wallet_info
        },
    },
    actions: {
        getWalletInfo({commit, rootState}, {id = 1, url = this.state.WallET_URL}) {
            axios.get(url, {params: {id: id}})
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_WALLET_INFO', x.data)
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

        makeTransfer({commit, rootState}, {url = this.state.MAKE_TRANSFER_URL, data = {}}) {
            axios.post(url, data)
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
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

