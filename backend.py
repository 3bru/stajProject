import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS staj1 (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO staj1 VALUES(NULL, ?, ?, ?, ?)",
                         (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM staj1")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="",
               isbn=""):  # default parameters handle empty arguments for select query
        self.cur.execute("SELECT * FROM staj1 WHERE title=? OR author=? OR year=? OR isbn=?",
                         (title, author, year, isbn))  # null creates id automatically
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE staj1 set title=?, author=?, year=?, isbn=? WHERE id=?",
                         (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):  # executed when this instance is deleted

        self.conn.close()