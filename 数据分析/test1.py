import link_mysql
from link_mysql import Link_mysql

mysql=Link_mysql('test_db')
mysql.create_table('user_info',[
    'user_name','varchar(20)',
    'password','varchar(20)'
])
mysql.create_table('students_info',[
    'name','varchar(20)',
    'chinese','int',
    'math','int',
    'english','int'    
])
