import requests
import pymysql


class aiqiyi():
    def __init__(self):
        self.db = pymysql.connect(user='root', password='root', db='spider')
        self.cursor = self.db.cursor()
        self.url = 'https://mesh.if.iqiyi.com/portal/videolib/pcw/data?version=1.0&ret_num=30&page_id={}&device_id=cdbc28b5acffb8fe882248c52cb479b0&passport_id=&recent_selected_tag=%E7%BB%BC%E5%90%88%3B%E5%86%85%E5%9C%B0&recent_search_query=&ip=202.108.14.240&scale=150&channel_id=2&tagName=&mode=24&three_category_id_v2=8052642132978633'
        self.headers = {
            'user agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'}

    def creat_table(self):
        sql = '''
                CREATE TABLE IF NOT EXISTS aqy(
                    id int primary key auto_increment not null,
                    name VARCHAR(255) NOT NULL, 
                    introducation VARCHAR(255) NOT NULL, 
                    jishu VARCHAR(255) NOT NULL

            )

        '''
        try:
            self.cursor.execute(sql)
            print("CREATE TABLE SUCCESS.")
        except Exception as ex:
            print(f"CREATE TABLE FAILED,CASE:{ex}")

    def get_data(self):
        for i in range(1, 5):
            response = requests.get(self.url.format(i), headers=self.headers)
            res_json = response.json()
            self.parse_data(res_json)

    def parse_data(self, data):
        for node in data['data']:
            item = {}
            item['name'] = node['title']
            item['introducation'] = node['desc']
            item['jishu'] = node['dq_updatestatus']
            self.save_data(item)

    def save_data(self, item):
        sql = 'insert into aqy(id,name,introducation, jishu) values (%s, %s, %s, %s)'
        try:
            self.cursor.execute(sql, (0, item['name'], item['introducation'], item['jishu']))
            # 提交到数据库执行
            self.db.commit()
            print('插入成功！')
        except Exception as e:
            print(f'mysql data error: {e}')
            # 错误进行回滚
            self.db.rollback()

    def main(self):
        self.creat_table()
        self.get_data()


if __name__ == '__main__':
    aqy = aiqiyi()
    aqy.main()