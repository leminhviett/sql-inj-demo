import sqlite3

conn = sqlite3.connect("data.db")
q = "select * from users"
res = conn.execute(q)

for r in res:
    print(r)

conn.close()