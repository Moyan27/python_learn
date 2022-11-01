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
    #添加数据
    def add_data(self,table_name,value_tuple):
        sql='insert into {} values {};'.format(table_name,','.join(str(i)for i in value_tuple))
        self.cur.execute(sql)
        self.db.commit()
    
    #查看建表结构
    def show_creat_table_info(self,table_name):
        sql='show create table {}'.format(table_name)
        self.cur.execute(sql)
        data=list(self.cur.fetchall())[0]
        data=list(data)
        print('表名：',data[0])
        print('建表语句：',data[1])
    
    #   

    #查询一个表
    def select_data(self,table_name,query_type,by_where=None,key='*'):
        if query_type=='direct':
            sql='select {} from {};'.format(key,table_name)
            self.cur.execute(sql)
            data=self.cur.fetchall()
        elif query_type=='by_where':
            sql='select {} from {} where {};'.format(key,table_name,by_where)
            self.cur.execute(sql)
            data=self.cur.fetchall()
            print(list(data))
        return data       
        
    def colse_database(self):
        self.db.commit()  
        self.cur.close()
        self.db.close()
    
    def run(self):
        self.colse_database()

if __name__=="__main__":
    mysql=Link_mysql('test_db')
    # mysql.create_table('usr',[
    #     'name','varchar(20)',
    #     'age','int'
    # ])
    #mysql.create_table('table_name')
    #mysql.show_creat_table_info('user_info')
    #mysql.add_data('user_info', [
    #    ('root','951127'),
    #    ('zhanyan','951127'),
    #    ('zy','123456')
    #])
    #data1=mysql.select_data(table_name='user_info', query_type='direct')
    #print(data1)
    #data2=mysql.select_data(table_name='user_info', query_type='by_where',by_where="user_name='root'")
    #print(data2)