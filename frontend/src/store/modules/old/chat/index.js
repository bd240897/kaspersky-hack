import axios from "axios";

export default ({
    namespaced: true,
    state() {
        return {
            chatHistory: {},
        }
    },
    getters: {},
    mutations: {
        SET_CHAT_HISTORY(state, chatHistory) {
            state.chatHistory = chatHistory.reverse()
        },
    },
    actions: {
        // TODO get dialog id

        getChatHistory({commit, rootState}, {
            url = this.state.CHAT_HISTORY_URL,
            dialogId = this.state.profile.id_dialog,
            limit = 10
        }) {
            axios.get(url, {
                params: {dialogId: dialogId, limit: limit},
            })
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');
                    commit('SET_CHAT_HISTORY', x.data.messages)
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
                });

        },

        sendMassage({commit, rootState}, {url = this.state.SEND_MSG_URL, data = {}}) {
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

