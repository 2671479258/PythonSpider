const CryptoJS = require('crypto-js')
function l(e) {
        var n = CryptoJS.enc.Latin1.parse("h5LoginKey123456")
          , a = CryptoJS.enc.Latin1.parse("h5LoginIv1234567")
          , t = e
          , o = CryptoJS.AES.encrypt(t, n, {
            iv: a,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.ZeroPadding
        });
        return o.toString()
    }

function encryptAES(e) {
            return l(e)
     }

function get_pw(pw) {
    password=encryptAES(pw)
    return password
}
pw=get_pw('1111')



data='rWPHL1699076096NyKFTOaXUYf'
TDFingerprint = data
var blackBoxMd5Value = CryptoJS.MD5(data).toString()


account='112321321321'
var n = Math.random()
pic_url='https://hotel.bestwehotel.com/api'+ "/safeverify/getImageVerify?mobile=" + account + "&verifyImageKey=" + n;
