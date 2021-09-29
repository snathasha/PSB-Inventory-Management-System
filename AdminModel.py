
from Conn import Conn


class AdminModel(Conn):

    def auth(self, username, password):
        super()
        val = (username, password)

        mycursor = self.conn.cursor()
        mycursor.execute(
            "SELECT * FROM admins WHERE username = %s AND password = %s LIMIT 1", val)
        myresult = mycursor.fetchall()
        self.conn.close()

        if myresult:
            return True
        return False


# AdminModel().auth("admin", "1234")
