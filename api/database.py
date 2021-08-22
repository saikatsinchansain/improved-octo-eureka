import mysql.connector

config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'service_backend',
  'raise_on_warnings': True
}

def get_db_conn():
    return mysql.connector.connect(**config)