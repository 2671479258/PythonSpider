import random
import requests
import json
import hashlib

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'doyo_pv=bfed519511ce4884213c8ebc7b6fac68; PHPSESSID=i9os3covhuavgjfb9j87lvegn7; doyo_www_uv_mark=true; Hm_lvt_b0affa74a0ef00f793803b2ae8a25f8a=1699447041; Hm_lpvt_b0affa74a0ef00f793803b2ae8a25f8a=1699447657',
    'Pragma': 'no-cache',
    'Referer': 'https://www.doyo.cn/passport/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
random=random.random()
params = {
    'username': 'a123456',
    'random': random,
}

response = requests.get('https://www.doyo.cn/User/Passport/token', params=params, headers=headers)
res=json.loads(response.text)
nonce=res['nonce']
ts=res['ts']
pw='123456'
sha1 = hashlib.sha1()
pw1=sha1.update(pw.encode('utf-8'))
pwstr=sha1.hexdigest()

dd = nonce + str(ts) + pwstr

sha2 = hashlib.sha1()
pwd2=sha2.update(dd.encode('utf-8'))

pw2str=sha2.hexdigest()
print(pw2str)




