
var CryptoJS = require('crypto-js')

u = function(t) {
                var e = CryptoJS.enc.Utf8.parse("G3JH98Y8MY9GWKWG")
                  , n = CryptoJS.enc.Utf8.parse(t)
                  , a = CryptoJS.AES.encrypt(n, e, {
                    mode: CryptoJS.mode.ECB,
                    padding: CryptoJS.pad.Pkcs7
                });
                return encodeURIComponent(a.toString())
            }


console.log(u('123456'));
