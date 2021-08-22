import mysql.connector

config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'service_backend',
  'raise_on_warnings': True
}

def connectdb():
    return mysql.connector.connect(**config)

def fetch_query(query):
    connection = connectdb()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data
 