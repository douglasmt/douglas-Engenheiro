import sqlite3
conn = sqlite3.connect("my_friends.db")

# data = ("Pitoco", "Pinscher Louco", 7)
# query = "INSERT INTO dogs VALUES (?,?,?);"
data = ("Floki", "Beagle", 12)
query = "INSERT INTO dogs VALUES (?,?,?);"

c = conn.cursor()
c.execute(query,data)
conn.commit()
conn.close()

