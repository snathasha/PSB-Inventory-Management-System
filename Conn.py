import mysql.connector


class Conn:
    def __init__(self):
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="jana30111998",
                database="ims",
                auth_plugin='mysql_native_password'
            )
            self.conn = con
            print('connet')
        except Exception as e:
            print(e)
