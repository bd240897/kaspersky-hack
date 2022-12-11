
let WS_URL = "wss://hack.invest-open.ru/chat"

let TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEwMDUwMSwibG9naW4iOiJ0ZXN0T3BlcmF0b3IiLCJyb2xlIjoiT1BFUkFUT1IiLCJpYXQiOjE2NjgxMDYyMjZ9.TO0GxhQqOAqT5j2a8_VlPVfpFij48cu28R39NCHxow8"

let token = "Replace_this_with_your_JWT_token";
let options = {
    extraHeaders: {
        "Authorization" : "JWT " + TOKEN
    }
};
// https://stackoverflow.com/questions/23406163/socket-io-client-how-to-set-request-header-when-making-connection

var socket = io(WS_URL, options);

socket.on('welcome', function (data) {
    console.log(data)
});
socket.on('time', function (data) {
    console.log(data)
});

socket.on('error', console.error.bind(console));

socket.on('message', console.log.bind(console));