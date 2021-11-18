import psycopg2
import json
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, AsIs
from django.core.management.utils import get_random_secret_key  


user_name = input('Input PostgreSQL username:')
password = input('Input PostgreSQL password:')
db_user_name = input('Input new Django username:')
db_name = input('Input new Django DB name:')
host = input("Input Host:")

con = psycopg2.connect(dbname='postgres',
      user=user_name, host=host,
      password=password)

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 

cur = con.cursor()

cur.execute("create user %s with password %s", (AsIs(db_user_name), password)) 
cur.execute(sql.SQL("CREATE DATABASE {} OWNER {}").format(
        sql.Identifier(db_name),sql.Identifier(db_user_name))
    )

cur.close()
con.close()

with open('core/config.json', 'w', encoding='utf-8') as f:
    json.dump({'DB_USER':db_user_name, 'DB_PASSWORD':password,
     'DB_NAME':db_name, 'DB_HOST':host, 'SECRET_KEY':get_random_secret_key()}, f, ensure_ascii=False, indent=4)



