import requests
import re
import json
import hashlib


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://login.lvmama.com',
    'Pragma': 'no-cache',
    'Referer': 'https://login.lvmama.com/nsso/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
session=requests.Session()
response = session.get('https://login.lvmama.com/nsso/login', headers=headers)
match = re.search(r'<input type="hidden" name="token" value="([^"]+)"/>', response.text)
token = match.group(1)
print(token)


pw='123456'
md=hashlib.md5(pw.encode())
password=md.hexdigest()	# md5加密
print(password)

data = {
    'userName': '18138447731',
    'password': password,
    'verifyCode': '',
}
response2 = session.post(
    'https://login.lvmama.com/nsso/geetest/login/validateNormalLogin.do',
    headers=headers,
    data=data,
).text
response_json = json.loads(response2)

# 提取securityCode的值
security_code = response_json.get('securityCode')

print(security_code)


