import sqlite3

conn = sqlite3.connect("../data/fitness.db")

cur = conn.cursor()

cur.execute(
    "UPDATE workouts SET workout_duration = ? WHERE id = ?",
    (80, 1)
)

cur.execute(
    "SELECT * from workouts where id = ?",
    (1,)
)
rows = cur.fetchall()
print(rows)

cur.execute(
    "UPDATE workouts SET workout_notes = ? WHERE workout_notes IS NULL",
    ("No None",)
)

cur.execute(
    "SELECT workout_notes from workouts",
)
rows = cur.fetchall()
print(rows)


conn.commit()
conn.close()