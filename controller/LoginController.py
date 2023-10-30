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
            if connection.is_connected():
                LoginController.message = "Connected"
                return connection
    except Exception as e:
        messagen = e
@staticmethod
def Close(self, connection):
    connection.Close()
