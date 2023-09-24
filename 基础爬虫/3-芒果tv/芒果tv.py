import requests
import pymysql

class Mangguo():
    def __init__(self):
        self.db = pymysql.connect(user='root', password='root', db='spider')
        self.cursor = self.db.cursor()
        self.url='https://pianku.api.mgtv.com/rider/list/pcweb/v3?allowedRC=1&platform=pcweb&channelId=50&pn=2&pc=80&hudong=1&_support=10000000&kind=87&area=a1&edition=a1&sort=c2'
        self.headers={'user agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'}

    def create_table(self):
        sql = '''
                        CREATE TABLE IF NOT EXISTS mgtv(
                            id int primary key auto_increment not null,
                            title VARCHAR(255) NOT NULL, 
                            story VARCHAR(255) NOT NULL, 
                            updateInfo VARCHAR(255) NOT NULL,
                            year VARCHAR (255) Not NULL

                    )

                '''
        try:
            self.cursor.execute(sql)
            print("CREATE TABLE SUCCESS.")
        except Exception as ex:
            print(f"CREATE TABLE FAILED,CASE:{ex}")

    def get_data(self):
        for i in range(1,4):
            response=requests.get(self.url.format(i),headers=self.headers)
            self.parse_data(response.json())

    def parse_data(self,data):
        for node in data['data']['hitDocs']:
            item={}
            item['title']=node['title']
            item['story'] = node['story']
            item['updateInfo'] = node['updateInfo']
            item['year']=node['year']
            self.save_data(item)

    def save_data(self,item):
        sql = 'insert into mgtv(id,title,story, updateInfo,year) values (%s, %s, %s, %s, %s)'
        try:
            self.cursor.execute(sql, (0, item['title'], item['story'], item['updateInfo'],item['year']))
            # 提交到数据库执行
            self.db.commit()
            print('插入成功！')
        except Exception as e:
            print(f'mysql data error: {e}')
            # 错误进行回滚
            self.db.rollback()


    def main(self):
        self.create_table()
        self.get_data()

if __name__ == '__main__':
    mgtv=Mangguo()
    mgtv.main()