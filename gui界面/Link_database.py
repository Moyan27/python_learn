import pymysql

class Link_database():
    def __init__(self):
        # 创建连接
        self.db = pymysql.connect(
            host='localhost',  # 连接地址, 本地
            user='root',  # 用户
            password='951127',  # 数据库密码
            port=3306,  # 端口,默认为3306
            charset='utf8',  # 编码
            database='test'  # 选择数据库
        )
        # 创建游标对象
        self.cur = self.db.cursor()

        # # MySQL语法
        # sql ='insert into user_info (name,passwrod),;'
        # # 执行sql
        # self.cur.execute(sql)
        # datas = self.cur.fetchall()
    def commit(self):
        # 提交信息
        self.db.commit()
        # 关闭
        #self.cur.close()
        self.db.close()

if __name__ == '__main__':
    link_database=Link_database()

