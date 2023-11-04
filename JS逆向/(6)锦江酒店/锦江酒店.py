import requests
import execjs
import ddddocr
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'c=4CIxQ7sF-1694874941083-4c391b2782b4e1672302239; gdp_user_id=bd0bf7d8-12c8-4eae-b710-8c2304d62483; HWWAFSESTIME=1699068125813; HWWAFSESID=436357f69c0d9c0dd1; Hm_lvt_b6e767c4467dcad9be907eab9e9c78ac=1697805089,1699022515,1699068127; Hm_lpvt_b6e767c4467dcad9be907eab9e9c78ac=1699076546; _fmdata=sBhbaLAurt3BlCva1ecYKf0VlQYgMSl0VrrFhzNjhcNDJqz%2FvGeDEMEDZ2wxliqDTReR3yHjTQldKE%2FyNa%2BGZA%3D%3D; _xid=0ertexxbC2qRnovAhlpHgCrr5VweTiNlsRIiUeRgQys%3D; 989d198a589474f0_gdp_session_id=33588a24-7082-44b0-b804-b360c808926e; 989d198a589474f0_gdp_sequence_ids=%7B%22globalKey%22%3A150%2C%22VISIT%22%3A7%2C%22PAGE%22%3A29%2C%22VIEW_CLICK%22%3A40%2C%22VIEW_CHANGE%22%3A77%7D; 989d198a589474f0_gdp_session_id_33588a24-7082-44b0-b804-b360c808926e=true',
    'Origin': 'https://hotel.bestwehotel.com',
    'Pragma': 'no-cache',
    'Referer': 'https://hotel.bestwehotel.com/NewLogin/?go=https%3A%2F%2Fhotel.bestwehotel.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-WE-SDK': '1.5.5',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

with open('锦江.js', 'r') as js_file:
    javascript_code = js_file.read()

# 创建一个 JavaScript 环境
ctx = execjs.compile(javascript_code)
password = ctx.eval('pw')
TDFingerprint=ctx.eval('TDFingerprint')
blackBoxMd5Value=ctx.eval('blackBoxMd5Value')
verifyImageKey=ctx.eval('n')
params = {
    'mobile': '112321321321',
    'verifyImageKey': verifyImageKey,
}
session = requests.Session()
img_res = session.get(
    'https://hotel.bestwehotel.com/api/safeverify/getImageVerify',
    params=params,
    headers=headers,
).content
with open ('./code.jpg', 'wb') as fp:
    fp.write (img_res)


ocr = ddddocr.DdddOcr(show_ad=False)
with open ('code.jpg', 'rb') as f:
    img_bytes = f.read ()
res = ocr.classification (img_bytes)  # 解析到的验证码数据
print (res)


json_data = {
    'groupTypeId': 2,
    'type': 1,
    'mobile': '112321321321',
    'password': password,
    'rememberMe': False,
    'verifyCode': res,
    'TDFingerprint': TDFingerprint,
    'blackBoxMd5': blackBoxMd5Value,
    'did': '8388228aaafee0e225d2bc45261a2b90',
    'deviceInfo': {
        'fingerPrintJs': 'b9295ec13a276cf674f69c77df044efd',
        'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'platform': 'Win32',
    },
}

response = session.post('https://hotel.bestwehotel.com/api/member/login', headers=headers, json=json_data)
print(response.text)


