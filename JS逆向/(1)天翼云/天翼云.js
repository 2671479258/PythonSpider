const CryptoJS = require('crypto-js')

function H() {
            var e, n, t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 32, r = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 16, a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split(""), o = [];
            if (r = r || a.length,
            t)
                for (e = 0; e < t; e++)
                    o[e] = a[0 | Math.random() * r];
            else
                for (o[8] = o[13] = o[18] = o[23] = "-",
                o[14] = "4",
                e = 0; e < 36; e++)
                    o[e] || (n = 0 | 16 * Math.random(),
                    o[e] = a[19 === e ? 3 & n | 8 : n]);
            return o.join("")
        }

comParam_seqCode=H()



var n = Date.now() - '-439'
var t = "s54zv9bm1vd5czfujy6nnuxj1l4g2ny6"
              , r = H()
              , a = CryptoJS.MD5((n + r + CryptoJS.MD5((r + t + n)).toString())).toString()


comParam_curTime=n
comParam_signature=a



function encryptByDES(e) {
            var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : ""
              , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {}
              , r = t.enc
              , a = void 0 === r ? "Utf8" : r
              , o = t.mode
              , c = void 0 === o ? "ECB" : o
              , i = t.padding
              , u = void 0 === i ? "Pkcs7" : i
              , d = CryptoJS.enc[a].parse(n)
              , l = {
                mode: CryptoJS.mode[c],
                padding: CryptoJS.pad[u]
            }
              , s = CryptoJS.TripleDES.encrypt(e, d, l);
            return s.toString()
        }
var pw="yhy2001nb!"
var account="2671479258@qq.com"
password=encryptByDES(pw,account+'00000000000')


params = {
    'referrer': 'wap',
    'mainVersion': '300031500',
    'comParam_curTime': comParam_curTime,
    'comParam_seqCode': comParam_seqCode,
    'comParam_signature': comParam_signature,
    'isCheck': 'true',
    'locale': 'zh-cn',
}

data = {
    'userName': account,
    'password': password,
}
console.log(params);
console.log(data);



