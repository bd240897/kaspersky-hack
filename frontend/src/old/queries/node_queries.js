const axios = require('axios');
const {createHash} = require('crypto');
var CryptoJS = require("crypto-js");

// full url
let CHAT_HISTORY = "https://hack.invest-open.ru/chat/history";
let CHAT_SEND = "https://hack.invest-open.ru/message/send";
let CHAT_LIST_DIALOGS = 'https://hack.invest-open.ru/chat/dialog'
let LOGIN = "https://hack.invest-open.ru/auth"
let IS_TOKEN_VALID = "https://hack.invest-open.ru/jwt/verify"

// path url
let BASE_URL = 'https://hack.invest-open.ru'
let CHAT_HISTORY_v2 = "/chat/history";
let CHAT_SEND_v2 = "/message/send";
let CHAT_LIST_DIALOGS_v2 = '/chat/dialog'
let LOGIN_v2 = "/auth"
let IS_TOKEN_VALID_v2 = "/jwt/verify"
let USER_INFO_v2 = "/user/info"

let TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEwMDUwMSwibG9naW4iOiJ0ZXN0T3BlcmF0b3IiLCJyb2xlIjoiT1BFUkFUT1IiLCJpYXQiOjE2NjgxMDYyMjZ9.TO0GxhQqOAqT5j2a8_VlPVfpFij48cu28R39NCHxow8"

function getChatHistory({url = CHAT_HISTORY, dialogId = 1, limit = 10}) {
    axios.get(url, {
        params: {dialogId: dialogId, limit: limit,},
        headers: {
            Authorization: 'Bearer ' + TOKEN
        }
    })
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
}

// default config

const instance = axios.create({
    baseURL: BASE_URL,
    headers: {
        Authorization: 'Bearer ' + TOKEN
    }
});


function getChatHistory_v2({url = CHAT_HISTORY_v2, dialogId = 1, limit = 10}) {
    // получить список сообщений по id диалога

    instance.get(url, {
        params: {dialogId: dialogId, limit: limit,},
    })
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
}


let data_send = {
    "message": {
        "dialogId": 1,
        "text": "Привет всем участникам Hack & Change!",
        "messageType": "WIDGET",
        "data": "{\"widget\":\"custom data\"}",
        "mediaUrl": "https://cdn-icons-png.flaticon.com/512/945/945244.png"
    }
}


// default config v2

axios.defaults.headers.common['Authorization'] = 'Bearer ' + TOKEN;
axios.defaults.baseURL = BASE_URL;

function sendMassage_v2({url = CHAT_SEND_v2, data = data_send}) {
    // получить список сообщений по id диалога

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
}

function getDialogs({url = CHAT_LIST_DIALOGS_v2}) {
    // получить список сообщений по id диалога

    axios.get(url)
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
}

// login: jordan   password: jordan_839  role: CLIENT
// login: ireland  password: ireland_839  role: OPERATOR

axios.defaults.headers.common['Authorization'] = ''


function hash(string) {
    // return createHash('sha256').update(string).digest('hex');
    return CryptoJS.SHA256(string).toString(CryptoJS.enc.hex);
}


data_login_global = {
    "login": "testUser",
    "password": "872e4e50ce9990d8b041330c47c9ddd11bec6b503ae9386a99da8584e9bb12c4"
}

data_login_cliend = {
    "login": "jordan",
    "password": hash("jordan_839")
}

data_login_operator = {
    "login": "ireland",
    "password": hash("ireland_839")
}

function login({url = LOGIN_v2, data = data_login_operator}) {
    // получить список сообщений по id диалога

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
}

data_token = {"jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEwMDUwMCwibG9naW4iOiJ0ZXN0VXNlciIsImlhdCI6MTY2ODAyMjMzNn0.kOHhWYX5uGulDr_xQ1h6QrGs_bb6ubzjacq6EodivYs"}


function tokenValid({url = IS_TOKEN_VALID_v2, data = data_token}) {
    // получить список сообщений по id диалога

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
}

axios.defaults.headers.common['Authorization'] = 'Bearer ' + TOKEN;

function getUserInfo({url = USER_INFO_v2, userId = 100500}) {
    // получить список сообщений по id диалога

    axios.get(url, {
        params: {userId: userId},
    })
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
}

let data_msg = {
    "message": {
        "dialogId": 1,
        "text": "Привет всем участникам Hack & Change!",
        "messageType": "WIDGET",
        "data": "{\"widget\":\"custom data\"}",
        "mediaUrl": "https://cdn-icons-png.flaticon.com/512/945/945244.png"
    }
}

function sendMassage({url = "/message/send", data=data_msg}) {
    // получить список сообщений по id диалога

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
}


// run
// getChatHistory({})
// getChatHistory_v2({})
// sendMassage_v2({})
// getDialogs({})
// login({})
// tokenValid({})
// getUserInfo({})
// sendMassage({})