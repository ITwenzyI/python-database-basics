import sqlite3
conn = sqlite3.connect("../../data/fitness.db")
cur = conn.cursor()


# Top3 längsten Workouts
cur.execute("""
SELECT workout_date, workout_type, workout_duration
FROM workouts
ORDER BY workout_duration DESC
LIMIT 3
""")
i = 1
for date, wtype, dur in cur.fetchall():
    print(f"Platz {i} am {date}: {wtype} {dur} Minutes.")
    i = i + 1





conn.commit()
conn.close()
