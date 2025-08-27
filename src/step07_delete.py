import sqlite3

conn = sqlite3.connect("../data/fitness.db")

cur = conn.cursor()

cur.execute("DELETE FROM workouts WHERE workout_notes IS ?", ("Test",))

cur.execute("SELECT * FROM workouts")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()