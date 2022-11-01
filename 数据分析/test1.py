import link_mysql
from link_mysql import Link_mysql

mysql=Link_mysql('test_db')
data=mysql.select_data(table_name='user_info', query_type='by_limit',by_limit=[1,3])
print(data)
data1=mysql.select_data(table_name='user_info', query_type='default')
print(data1)