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
        data_new=dict({
            '表名':data[0],
            '建表语句':data[1]
        })
        return data_new
        #print('表名：',data[0])
        #print('建表语句：',data[1])

    #查询一个表
    def select_data(self,table_name,query_type,by_sc_value=None,by_where=None,key='*',by_sc='desc',by_limit=[1,10],by_fixed=None):
        if query_type=='default':
            sql='select {} from {};'.format(key,table_name)
        elif query_type=='by_where':
            sql='select {} from {} where {};'.format(key,table_name,by_where)
        elif query_type=='by_sc':
            sql='select {} from {} order by {} {};'.format(key,table_name,by_sc_value,by_sc)
        elif query_type=='by_limit':
            for j in by_limit:
                if j==1:
                    by_limit[0]=0
            sql='select {} from {} limit {};'.format(key,table_name,','.join(str(i)for i in by_limit))
        elif query_type=='fixed':
            sql='select {} from {} {};'.format(key,table_name,by_fixed)
        self.cur.execute(sql)
        data=self.cur.fetchall()
        return data 
    #删除数据
    def delete_data(self,table_name,delete_type,by_fixed='',by_where='',key='*'):
        if delete_type=='default':
            sql='delete from {};'.format(table_name)
        elif delete_type=='by_where':
           sql='delete from {} where {};'.format(table_name,by_where)
        elif delete_type=='fixed':
            sql='delete from {} {};'.format(table_name,)
        self.cur.execute(sql)
        self.db.commit()
    
    #修改/更新表数据
    def update_data(self,table_name,update_type,update_value,by_where='',by_fixed=''):
        if update_type=='default':
            sql='update {} set {};'.format(table_name,update_value)
        elif update_type=='by_where':
            sql='update {} set {} where {}'.format(table_name,update_value,by_where)
        elif update_type=='fixed':
            sql='ipdate {} set {}'.format(table_name,update_value,by_fixed)
        self.cur.execute(sql)
        self.db.commit()
            
        
    def colse_database(self):
        self.db.commit()  
        self.cur.close()
        self.db.close()
    
    def run(self):
        self.colse_database()

if __name__=="__main__":
    mysql=Link_mysql('test')