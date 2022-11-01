import pymysql
  
class Link_mysql(object):
    def __init__(self,database):
        self.db =pymysql.connect(
            host='localhost',
            user='root',
            passwd='951127',
            db='{}'.format(database)
        )
        self.cur=self.db.cursor()
    #创建一个新表
    def create_table(self,table_name,value_list=['name','varchar(20)']):
        s=[]
        for index,a in enumerate(value_list):
            s.append(a)
            if index!=len(value_list)-1:
                if (index+1)%2==0:
                    s.append(',\n')
            elif index==len(value_list)-1:
                value_list=s
        sql='''
            create table {}(
                {}
            )default charset=utf8;
        '''.format(table_name,' '.join(value_list))
        self.cur.execute(sql)
    #查询一个表
    def select_data(self,table_name):
        sql='select * from {};'.format(table_name)
        self.cur.execute(sql)
        data=self.cur.fetchall()
        data_list=[]
        for i in data:
            data_list.append(i)
        return data_list        
        
    def colse_database(self):
        self.db.commit()  
        self.cur.close()
        self.db.close()
    
    def run(self):
        self.colse_database()

if __name__=="__main__":
    db=Link_mysql('test_db')
    # db.create_table('usr',[
    #     'name','varchar(20)',
    #     'age','int'
    # ])
    #db.create_table('table_name')