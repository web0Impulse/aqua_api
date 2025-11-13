from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): pass

server_port = 5001
mysql_user = 'user'
mysql_passw = 'pass'
db_name = 'db_name'
sqlalchemy_mysql_connection_string = \
f'mysql+pymysql://{mysql_user}:{mysql_passw}@localhost/{db_name}?charset=utf8'
mysql_connection = create_engine(sqlalchemy_mysql_connection_string)