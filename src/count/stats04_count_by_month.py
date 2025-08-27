import sqlite3
conn = sqlite3.connect("../../data/fitness.db")
cur = conn.cursor()


# Wie viele Workouts gab es im August 2025?
cur.execute("""
SELECT COUNT(*) FROM workouts WHERE workout_date LIKE ?
""", ("2025-08-%",))
print("August 2025:", cur.fetchone()[0])

cur.execute("""
SELECT COUNT(*) FROM workouts WHERE workout_date LIKE ? AND workout_type LIKE ?
""", ("2025-08-%", "Cardio"))
print("August 2025 only Cardio:", cur.fetchone()[0])



conn.commit()
conn.close()
