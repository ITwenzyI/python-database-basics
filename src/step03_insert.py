import sqlite3

conn = sqlite3.connect('../data/fitness.db')

cur = conn.cursor()

# cur.execute(
#     "INSERT INTO workouts (workout_date, workout_type, workout_duration, workout_notes) VALUES (?, ?, ?, ?)",
#
#     ("2025-08-26", "Beine", 60, "Erstes Training gespeichert")
# )

cur.execute(
    "INSERT INTO workouts (workout_date, workout_type, workout_duration) VALUES (?, ?, ?)",

    ("2025-08-20", "Beine", 80)
)

conn.commit()

conn.close()