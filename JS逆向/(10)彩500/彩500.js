var CryptoJS = require('crypto-js')


e={
    "userName": "1234567",
    "password": "123456"
}



function c(e, t) {
            return CryptoJS.MD5((e.toLowerCase() + CryptoJS.MD5(t).toString())).toString()
        }

function Login(e) {
                var t = "dafacloud_" + Math.random()
                  , n = {
                    random: encode(t)
                }

                  , i = c(e.userName, e.password);

                e.password = CryptoJS.MD5(i + t).toString(),
                e.random = n.random
    console.log(e);

}

cb_utob = function(t) {
                        if (t.length < 2)
                            return (e = t.charCodeAt(0)) < 128 ? t : e < 2048 ? fromCharCode(192 | e >>> 6) + fromCharCode(128 | 63 & e) : fromCharCode(224 | e >>> 12 & 15) + fromCharCode(128 | e >>> 6 & 63) + fromCharCode(128 | 63 & e);
                        var e = 65536 + 1024 * (t.charCodeAt(0) - 55296) + (t.charCodeAt(1) - 56320);
                        return fromCharCode(240 | e >>> 18 & 7) + fromCharCode(128 | e >>> 12 & 63) + fromCharCode(128 | e >>> 6 & 63) + fromCharCode(128 | 63 & e)
                    }
utob = function(t) {
                    re_utob = /[\uD800-\uDBFF][\uDC00-\uDFFFF]|[^\x00-\x7F]/g
                        return t.replace(re_utob, cb_utob)
                    }



function _encode(t) {
                        return btoa(utob(t))
                    }
encode = function(t, e) {
                        return e ? _encode(String(t)).replace(/[+\/]/g, function(t) {
                            return "+" == t ? "-" : "_"
                        }).replace(/=/g, "") : _encode(String(t))
                    }

Login(e)