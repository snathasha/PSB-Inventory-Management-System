
from Conn import Conn


class ItemModel(Conn):

    def get(self):
        super()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM items")
        list = cur.fetchall()
        self.conn.close()
        return list

    def create(self, name, cate, qty, price, date):
        super()
        val = (name, cate, qty, price, date)
        cur = self.conn.cursor()
        cur.execute(
            "insert into items (name, category, qty, price, date) values(%s,%s,%s,%s,%s)", val)
        self.conn.commit()
        self.conn.close()
        return True

    def update(self, id, name, cate, qty, price, date):
        super()
        val = (name, cate, qty, price, date, id)
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE items SET name = %s, category = %s, qty = %s, price = %s, date = %s WHERE id = %s", val)
        self.conn.commit()
        self.conn.close()
        return True

    def delete(self, id):
        super()
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM items WHERE id = " +
                        str(id))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return False

    def search(self, name):
        super()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM items WHERE name LIKE " +
                    "'"+str(name)+"%'")
        list = cur.fetchall()
        self.conn.close()
        return list

    def sort(self, order, col):
        super()
        val = (order, col)
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM items ORDER BY " +
                    str(col) + " " + str(order))
        list = cur.fetchall()
        self.conn.close()
        return list


#ItemModel().sort('qty', 'ASC')
# #ItemModel().create('test', 'test cate', 65, 65.00, '2020-01-01')ASC
# print(ItemModel().get())
