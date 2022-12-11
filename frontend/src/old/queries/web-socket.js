const WebSocket = require('ws');

let WS_URL = "wss://hack.invest-open.ru/chat"

let TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEwMDUwMSwibG9naW4iOiJ0ZXN0T3BlcmF0b3IiLCJyb2xlIjoiT1BFUkFUT1IiLCJpYXQiOjE2NjgxMDYyMjZ9.TO0GxhQqOAqT5j2a8_VlPVfpFij48cu28R39NCHxow8"

let token = "Replace_this_with_your_JWT_token";
let options = {
    headers: {
        "Authorization" : "JWT " + TOKEN
    }
};

let socket = new WebSocket(WS_URL, options);

socket.onopen = function(e) {
  console.log("[open] Соединение установлено");
  console.log("Отправляем данные на сервер");
  // socket.send("Меня зовут Джон");
};

socket.onmessage = function(event) {
  console.log(`[message] Данные получены с сервера: ${event.data}`);
};

socket.onclose = function(event) {
  if (event.wasClean) {
    console.log(`[close] Соединение закрыто чисто, код=${event.code} причина=${event.reason}`);
  } else {
    // например, сервер убил процесс или сеть недоступна
    // обычно в этом случае event.code 1006
    console.log('[close] Соединение прервано');
  }
};

// // To close the socket....
// socket.close()
