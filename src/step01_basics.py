import sqlite3

conn = sqlite3.connect("../data/fitness.db")



cur = conn.cursor()
print("Verbindung erfolgreich!")

conn.close()
