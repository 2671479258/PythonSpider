import requests
from lxml import etree
import os


class bizhi_36 ():
    def __init__ (self):
        self.url = 'https://www.3gbizhi.com/sjbz/index_{}.html'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    def get_data (self):
        for i in (1, 4):
            response = requests.get (self.url.format (i), headers=self.headers)
            html_data = etree.HTML (response.text)
            url_list = html_data.xpath ('//div[6]/ul/li/a/@href')
            for i in url_list:
                detail_url = i
                self.detail_data (detail_url)

    def detail_data (self, detail_url):
        res = requests.get (detail_url)
        res_html = etree.HTML (res.text)
        img_name = res_html.xpath ('//div[@class="mbm"]/h2/text()') [0]
        img_url = res_html.xpath ('//div[@class="showcontw mtw dispflex"]/div[1]/a/@href') [0]
        self.download_pic (img_name, img_url)

    def download_pic (self, iname, iurl):
        if not os.path.exists ('36壁纸'):
            os.mkdir ('36壁纸')
        response = requests.get (iurl)
        with open ('36壁纸/' + str (iname) + '.png', 'wb')as f:
            f.write (response.content)
            print (iname + '保存成功')

    def main (self):
        self.get_data ()


if __name__ == '__main__':
    Bizhi_36 = bizhi_36 ()
    Bizhi_36.main ()
