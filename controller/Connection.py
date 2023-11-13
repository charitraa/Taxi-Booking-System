import mysql.connector as c
class Database:
    message = ""
    try:
        @staticmethod
        def Connect():
            connection = c.connect(
                host='localhost',
                user = 'root',
                password = 'root',
                database = 'taxi'
            )
            if connection.is_connected():
                Database.message = "Connected"
                return connection
            connection.close()  
    except Exception as e:
        print(e)