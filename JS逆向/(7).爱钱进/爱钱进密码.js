var CryptoJS = require('crypto-js')
password='123456'
m=CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(password))
function encode(a, b) {
            return b ? m(String(a)).replace(/[+\/]/g, function(a) {
                return "+" == a ? "-" : "_"
            }).replace(/=/g, "") : m
        }

encodedData=encode(password)

