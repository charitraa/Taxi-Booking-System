import mysql.connector as c

class LoginController:
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
            connection.close()
            if connection.is_connected():
                LoginController.message = "Connected"
                return connection
            connection.close()
        
    except Exception as e:
        messagen = e

