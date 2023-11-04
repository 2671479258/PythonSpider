passwd='123456'
getKeyPair = function(e, t, i) {
            return new p(e,t,i)
        }

var p = function p(e, t, i) {
            var n = b;
            te = biFromHex(e),
            this.d = n.biFromHex(t),
            this.m = n.biFromHex(i),
            this.chunkSize = 2 * n.biHighIndex(this.m),
            this.radix = 16,
            this.barrett = new a.BarrettMu(this.m)
        };
function biFromHex(e) {
            for (var t = new C, i = e.length, n = 0; 0 < i; i -= 4,
            ++n)
                t.digits[n] = b.hexToDigit(e.substr(Math.max(i - 4, 0), Math.min(i, 4)));
            return t
        }
function rsaFun(e) {
                    var t = getKeyPair("10001", "", "ab86b6371b5318aaa1d3c9e612a9f1264f372323c8c0f19875b5fc3b3fd3afcc1e5bec527aa94bfa85bffc157e4245aebda05389a5357b75115ac94f074aefcd");
                    return n.rsaUtils.encryptedString(t, encodeURIComponent(e)).replace(/\s/g, "-")
                }



pw= rsaFun(passwd)
console.log(pw);