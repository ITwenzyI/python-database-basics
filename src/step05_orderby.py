import sqlite3

conn = sqlite3.connect('../data/fitness.db')

cur = conn.cursor()


# ASC = aufsteigend (klein → groß, alt → neu, alphabetisch). Standard, wenn du nichts angibst.
# DESC = absteigend (groß → klein, neu → alt)

cur.execute("select * from workouts order by workout_date DESC")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("select * from workouts order by workout_duration DESC LIMIT 1")
rows = cur.fetchall()
for row in rows:
    print(f"Limit {row}")

cur.execute("select * from workouts order by workout_duration DESC LIMIT 1 OFFSET 1")
rows = cur.fetchall()
for row in rows:
    print(f"Limit with Offset {row}")

cur.execute("select * from workouts order by workout_type ASC, workout_date DESC")
rows = cur.fetchall()
for row in rows:
    print(row)
