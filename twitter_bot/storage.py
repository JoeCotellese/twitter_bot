import sqlite3
import time

class Storage():
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)

    def save_user(self, username):
        insert_string = """
        INSERT into twitter_users (username,follow_date) values ('{}', {})
        """.format(username, int(time.time()))
        c = self.conn.cursor()
        c.execute(insert_string)
        self.conn.commit()
        return
    
    def get_user(self, username):
        c = self.conn.cursor()
        results = c.execute("SELECT * FROM twitter_users WHERE username=?",(username,))
        return results.fetchone()
    
    def remove_user(self, username):
        c = self.conn.cursor()
        results = c.execute("DELETE from twitter_users where username=?", (username, ))
        self.conn.commit()
        return results
        