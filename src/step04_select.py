import sqlite3

conn = sqlite3.connect('../data/fitness.db')

cursor = conn.cursor()

cursor.execute("select * from workouts")
rows = cursor.fetchall()
# rows = cursor.fetchmany(2)
# rows = cursor.fetchone()

for row in rows:
    print(f"ID: {row[0]}, Datum: {row[1]}, Type: {row[2]}, Time: {row[3]}, Notes: {row[4]}")

cursor.execute("select workout_date from workouts")
rows = cursor.fetchall()
for row in rows:
    print("Workout date:", row[0])

cursor.execute("select * from workouts where workout_type = ?", ('Cardio',))
rows = cursor.fetchall()
for row in rows:
    print("ID with Type Cardio:", row[0])

cursor.execute("select * from workouts where workout_duration > ?", (60,))
rows = cursor.fetchall()
for row in rows:
    print("ID with duration above 60:", row[0])

conn.close()