var SHA256 = require("crypto-js/sha256");
var CryptoJS = require("crypto-js");
const { createHash } = require('crypto');

var hash = CryptoJS.SHA256("Message").toString(CryptoJS.enc.Base64);
console.log(hash);
//
// let a = createHash('sha256').update("Message").digest('hex');
// console.log(a);
