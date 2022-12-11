import axios from "axios";
import router from '../../../router'

export default ({
    namespaced: true,
    state() {
        return {
            profile_info: {},
            wallets_list: [],
        }
    },
    getters: {},
    mutations: {
        SET_PROFILE_INFO(state, userInfo) {
            state.profile_info = userInfo
        },
        SET_WALLETS_LIST(state, wallets_list) {
            state.wallets_list = wallets_list
        },
    },
    actions: {
        getProfileInfo({commit, rootState}, {url = this.state.PROFILE_URL}) {
            axios.get(url)
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_PROFILE_INFO', x.data)
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
                    // if (err.response.status === 401) {
                    //     router.push({ name: 'Login'})
                    // }
                    return err
                })
        },

        getWalletsList({commit, rootState}, {url = this.state.WALLETS_LIST_URL}) {
            axios.get(url)
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_WALLETS_LIST', x.data)
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

        // getUserInfo({commit, rootState}, {url = this.state.USER_INFO_URL, userId = this.state.login.userId,}) {
        //     axios.get(url, {
        //         params: {userId: userId},
        //     })
        //         .then(function (x) {
        //             console.log(x.data)
        //             console.log('SUCCESS!!');
        //             commit('SET_USER_INFO', x.data)
        //         })
        //         .catch(err => {
        //             console.log(err)
        //             if (err.response) {
        //                 console.log("client received an error response (5xx, 4xx)")
        //             } else if (err.request) {
        //                 console.log("client never received a response, or request never left")
        //             } else {
        //                 console.log("anything else ")
        //             }
        //             return err
        //         })
        // },

        // getIdDialog({commit, rootState}, {url = this.state.CHAT_ID_DIALOG_URL}) {
        //     axios.get(url)
        //         .then(function (x) {
        //             console.log(x.data)
        //             console.log('SUCCESS!!');
        //             commit('SET_ID_DIALOG', x.data.dialogId)
        //
        //         })
        //         .catch(err => {
        //             console.log(err)
        //             if (err.response) {
        //                 console.log("client received an error response (5xx, 4xx)")
        //             } else if (err.request) {
        //                 console.log("client never received a response, or request never left")
        //             } else {
        //                 console.log("anything else ")
        //             }
        //             return err
        //         })
        // },
    },
})

