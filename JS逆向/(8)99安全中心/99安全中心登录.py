import requests
import re
import ddddocr
import execjs


headers = {
    'authority': 'checkcode.99.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'Hm_lvt_a91d620539bbc5cb3fee464ee5ace062=1697803620; 0FF535D2-3733-4059-AA48-73EFB0DA00CE=376FC8AE-EA0A-4aa9-8CF8-BDCF086DAFE7=2023-10-20+20%3A07%3A11&43CB770B-ECB7-4262-9F28-474C756FA85C=45766261-983c-f85e-b817-e495c83eb9d7&77A7D26A-7211-4b2a-A04A-1A3F9959F179=3085630804&BF191744-3205-4d76-B8FC-3E0387F7EEFE=e81abaf3450d79b296f85230700d1ea9; gosessionid=31e31dbe3561b6d43db0c11046462b13; h=y5-0.01101s',
    'pragma': 'no-cache',
    'referer': 'https://aq.99.com/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}
params = {
    'action': 'getticket',
    'bussiness': 'aq_login',
    'callback': 'jQuery112405638457490319551_1699104532525',
    '_': '1699102219926',
}

session=requests.Session()

response = session.get(url='https://checkcode.99.com/token', params=params,  headers=headers)
match = re.search(r'"ticket":"([^"]+)"', response.text)
ticket = match.group(1)





headers2 = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_a91d620539bbc5cb3fee464ee5ace062=1697803620; 0FF535D2-3733-4059-AA48-73EFB0DA00CE=376FC8AE-EA0A-4aa9-8CF8-BDCF086DAFE7=2023-10-20+20%3A07%3A11&43CB770B-ECB7-4262-9F28-474C756FA85C=45766261-983c-f85e-b817-e495c83eb9d7&77A7D26A-7211-4b2a-A04A-1A3F9959F179=3085630804&BF191744-3205-4d76-B8FC-3E0387F7EEFE=e81abaf3450d79b296f85230700d1ea9; ASP.NET_SessionId=im34lb45ieibrpudpd33kfrf; gosessionid=31e31dbe3561b6d43db0c11046462b13; h=y5-0.01101s',
    'Pragma': 'no-cache',
    'Referer': 'https://aq.99.com/V3/NDUser_Login.htm',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params2 = {
    'CallBack': 'jQuery112405638457490319551_1699104532525',
    'nduseraction': 'getverifycodestate',
    'verifycodetype': 'UserLogin',
    'bussiness': 'aq_login',
    'ticket': ticket,
    'SiteFlag': '995',
    'RND': '0.7535756301175676',
    '_': '1699104532527',
}

response2 = session.get('https://aq.99.com/AjaxAction/AC_verifycode.ashx', params=params2,headers=headers2)
match2 = re.search(r'"VerifyCodeUrl":"([^"]+)"', response2.text)
VerifyCodeUrl = match2.group(1)


img_res=requests.get(url=VerifyCodeUrl,headers=headers).content
with open ('./code.jpg', 'wb') as fp:
    fp.write (img_res)

ocr = ddddocr.DdddOcr(show_ad=False)
with open ('code.jpg', 'rb') as f:
    img_bytes = f.read ()
res = ocr.classification (img_bytes)  # 解析到的验证码数据


with open('99安全.js', 'r') as js_file:
    javascript_code = js_file.read()

# 创建一个 JavaScript 环境
ctx = execjs.compile(javascript_code)
password = ctx.eval('password')

print(res)


headers3 = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_a91d620539bbc5cb3fee464ee5ace062=1697803620; ASP.NET_SessionId=im34lb45ieibrpudpd33kfrf; gosessionid=31e31dbe3561b6d43db0c11046462b13; 0FF535D2-3733-4059-AA48-73EFB0DA00CE=376FC8AE-EA0A-4aa9-8CF8-BDCF086DAFE7=2023-11-04+21%3A25%3A02&43CB770B-ECB7-4262-9F28-474C756FA85C=45766261-983c-f85e-b817-e495c83eb9d7&77A7D26A-7211-4b2a-A04A-1A3F9959F179=3085630804&BF191744-3205-4d76-B8FC-3E0387F7EEFE=2e82274a6120ff6dd63080c46ea052ad; h=y5-0.00999s',
    'Pragma': 'no-cache',
    'Referer': 'https://aq.99.com/V3/NDUser_Login.htm',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
params_lg = {
    'CallBack': 'jQuery112405638457490319551_1699104532525',
    'siteflag': '995',
    'nduseraction': 'login',
    'txtUserName': '131384471232',
    'txtPassword': password,
    'checkcode': res,
    'Rnd': '0.10589798336121126',
    'aws': '2c5cccdb88757bf4ed168b4fe8640cde',
    '_': '1699104532528',
}

response3 = session.get('https://aq.99.com/AjaxAction/AC_userlogin.ashx', params=params_lg, headers=headers3)
print(response3.text)