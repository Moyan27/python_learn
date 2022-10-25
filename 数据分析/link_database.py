import pymysql

class Link_database(object):
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                     port=3306,
                                     user='root',
                                     password='951127',
                                     db='test',
                                     charset='utf8')
        self.cursor = self.connection.cursor()

    def show_tables(self):
        sql='show tables;'
        self.cursor.execute(sql)
        datas=self.cursor.fetchall()
        for i in datas:
            print(i)









if __name__ == "__main__":
    Link_database().show_tables()