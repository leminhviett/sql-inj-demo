import sqlite3

class UserModel:
    def __init__(self) -> None:
        self._conn = sqlite3.connect("data.db")

        try:
            self._conn.execute('''CREATE TABLE USERS
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME           TEXT    NOT NULL,
                PASSWORD           TEXT    NOT NULL,
                SALARY         REAL);''')
        except sqlite3.OperationalError as e:
            print(e)


    def addUser(self, user_name, pw, salary):
        check_existing = f"SELECT * from users where username = '{user_name}'"
        temp  = self._conn.execute(check_existing)

        if temp.rowcount >= 1:
            return None

        query = f"INSERT INTO users (USERNAME, PASSWORD, SALARY) VALUES (?, ?, ?);"
        self._conn.execute(query, (user_name, pw, salary))
        self._conn.commit()
        print(f'user {user_name} added')
        
    def getUser(self, user_name, pw):
        query = "SELECT * from users where username = '" + user_name + "' AND PASSWORD = '" + pw + "' LIMIT 1"
        res = self._conn.execute(query)
        print(query)
        for row in res:
            return {"username" : row[1], "salary" : row[3]}
        return None
    
    def close(self):
        self._conn.close()
        
