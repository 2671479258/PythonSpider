import base64
import requests
from lxml import etree
import time
import json
import urllib.parse
import random
import ddddocr


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=83953779BD13DF2ACF18D6CC9955C225; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


session = requests.Session()

response = session.get(
    'https://owssso.szse.cn/sso/login?service=https://www.szse.cn/application/userCenter/accountinfo/&locale=zh',
    headers=headers,
).text
tree = etree.HTML(response)
execution = tree.xpath('/html/body/main/div[2]/div[1]/form/div[4]/input[3]/@value')[0]
print(execution)




timestamp_in_seconds = time.time()
timestamp_in_milliseconds = int(timestamp_in_seconds * 1000)
params = {
    '_': timestamp_in_milliseconds,
}

code_response = session.get('https://owssso.szse.cn/sso/enuuid', params=params, headers=headers).text
data = json.loads(code_response)

# 提取uuid的值
uuid = data['uuid']
enuuid = data['enuuid']

random_number = random.random()

src = 'https://owssso.szse.cn/sso/'+'picture?receiver=' + uuid + '&enuuid=' + urllib.parse.quote(enuuid)+"&rand="+str(random_number)
img_res=session.get(url=src,headers=headers).content
with open ('./code.jpg', 'wb') as fp:
    fp.write (img_res)

ocr = ddddocr.DdddOcr(show_ad=False)
with open ('code.jpg', 'rb') as f:
    img_bytes = f.read ()
res = ocr.classification (img_bytes)  # 解析到的验证码数据
print (res)









#密码模块
decoded_data = '123456'
decoded_bytes = decoded_data.encode('utf-8')  # 将字符串转换为字节字符串
encoded_bytes = base64.b64encode(decoded_bytes)  # 编码字节字符串
encoded_data = encoded_bytes.decode('utf-8')  # 将编码后的字节字符串转换为字符串
print(encoded_data)