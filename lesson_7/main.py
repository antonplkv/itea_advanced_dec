import sqlite3

conn = sqlite3.connect('shop.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

query = "INSERT into products ('title') VALUES ('newproduct')"


cursor.execute(query, [1])

conn.commit()
conn.close()