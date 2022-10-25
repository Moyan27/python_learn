import pymysql

class Link_database(object):
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                     port=3306,
                                     user='root',
                                     password='951127',
                                     db='mysql',
                                     charset='utf8')
        pass








if __name__ == "__main__":
    Link_database()