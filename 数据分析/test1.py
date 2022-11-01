import sys,os
sys.path.append(os.path.dirname(__file__))
import link_test_db
from link_test_db import Link_mysql

Link_mysql('test_db')