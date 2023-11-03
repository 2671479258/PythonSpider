var window = {
    srcId: "", // 在这里定义window的属性
    // 其他属性和方法可以根据需要添加
};


function k(e, t) {
            t = T(t, e) ? [t] : O(t);
            for (var n = 0, r = t.length; null != e && n < r; )
                e = e[D(t[n++])];
            return n && n == r ? e : void 0
        }
o=(0,
                V)(window, "srcId", "")

function V(e, t, n) {
            var r = null == e ? void 0 : k(e, t);
            return void 0 === r ? n : r
        }

srcId=o