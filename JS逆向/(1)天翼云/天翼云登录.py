import requests
import execjs


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'ct_tgc=8bce448c-0527-4aeb-8ab7-6d445fc0982c; Hm_lvt_4b4ce93f1c92033213556e55cb65769f=1698932148; Hm_lpvt_4b4ce93f1c92033213556e55cb65769f=1698932148; sid1=1698932148578-703D155D2E0EECE384B5667BE45C93A4; sid2=1698932148578-703D155D2E0EECE384B5667BE45C93A4; pvid=1',
    'Origin': 'https://m.ctyun.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://m.ctyun.cn/wap/main/auth/login?redirect=%2Fmy',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-riskdevicesign': '200a1658ab584a9ad8f1ab4bfb4d099a',
}

with open('天翼云.js', 'r') as js_file:
    javascript_code = js_file.read()

# 创建一个 JavaScript 环境
ctx = execjs.compile(javascript_code)
params = ctx.eval('params')
data=ctx.eval('data')


session = requests.Session()

# Perform the login request
login_url = 'https://m.ctyun.cn/account/login'
response = session.post(login_url, params=params, headers=headers, data=data)

if response.status_code == 200:
    print("模拟登录成功")

# Now you can access another URL within the same session
other_url = 'https://m.ctyun.cn/account/queryPrivacyAccountInfo'
response = session.get(other_url,headers=headers,params=params)

if response.status_code == 200:
    print("查看个人主页成功")
    response.encoding = 'utf-8'
    print(response.text)
else:
    print("失败！")

# Don't forget to close the session when you're done
session.close()