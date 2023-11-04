import requests
import ddddocr
from lxml import etree
import execjs
if __name__ == '__main__':
    cookies = {
        'kefu': '0',
        'JSESSIONID': '996613170BDCF85AC6FF82581A4FE5C9',
        'imgBizId': 'd86f9bc73b4d4bf1b7150b4f2b6a6028',
        'Logger_Bi_Global_User_Id': '76894f6d-fd51-9fe1-0813-c7a59b288baa',
        'Hm_lvt_8fa6fa4b380c606c30da0abb5564a354': '1697698932',
        'Hm_lpvt_8fa6fa4b380c606c30da0abb5564a354': '1697698932',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'kefu=0; JSESSIONID=996613170BDCF85AC6FF82581A4FE5C9; imgBizId=d86f9bc73b4d4bf1b7150b4f2b6a6028; Logger_Bi_Global_User_Id=76894f6d-fd51-9fe1-0813-c7a59b288baa; Hm_lvt_8fa6fa4b380c606c30da0abb5564a354=1697698932; Hm_lpvt_8fa6fa4b380c606c30da0abb5564a354=1697698932',
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
    url = 'https://www.iqianjin.com/user/login'
    page_text = requests.get(url=url, headers=headers,cookies=cookies).text

    tree = etree.HTML(page_text)
    # 将验证码图片保存到了本地
    code_img_src = 'https://www.iqianjin.com/' + tree.xpath('//*[@id="loginForm"]/fieldset/div[3]/a[1]/img/@src')[0]
    code_data = requests.get(url=code_img_src, headers=headers).content
    with open('../code.jpg', 'wb') as fp:
        fp.write(code_data)
    # 解析验证码
    ocr = ddddocr.DdddOcr(show_ad=False)
    with open('../code.jpg', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes) # 解析到的验证码数据



    cookies = {
        'kefu': '0',
        'JSESSIONID': '3C8AC7697F19629285886CB47564E8A6',
        'imgBizId': 'a6c070baed49474bbd77e21956e897e9',
        'Hm_lvt_8fa6fa4b380c606c30da0abb5564a354': '1697698932,1697780850,1699082731',
        'Hm_lpvt_8fa6fa4b380c606c30da0abb5564a354': '1699082731',
        'Logger_Bi_Global_User_Id': '6da8d7d7-6395-c0ab-b8ce-9990e6f321f7',
    }

    with open('爱钱进密码.js', 'r') as js_file:
        javascript_code = js_file.read()

    # 创建一个 JavaScript 环境
    ctx = execjs.compile(javascript_code)
    password = ctx.eval('encodedData')


    data = {
        'name': '18138447743',
        'password': password,
        'code':res,
        'rememberMe': 'on',
    }

    response = requests.post('https://www.iqianjin.com/user/logon', cookies=cookies, headers=headers, data=data)
    print(response.text)


