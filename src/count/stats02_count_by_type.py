import sqlite3
conn = sqlite3.connect("../../data/fitness.db")
cur = conn.cursor()


# Wie viele Workouts pro Typ habe ich?
cur.execute("""
SELECT workout_type, COUNT(*) FROM workouts GROUP BY workout_type
""")
rows = cur.fetchall()
print(rows)
for wtype, cnt in rows:
    print(f"{wtype}: {cnt}")


conn.commit()
conn.close()
