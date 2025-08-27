import sqlite3
conn = sqlite3.connect("../../data/fitness.db")
cur = conn.cursor()


# Wie viele Workouts gibt es insgesamt?
cur.execute("SELECT COUNT(*) FROM workouts")
total = cur.fetchone()[0]
print(f"Gesamt: {total}")

conn.commit()
conn.close()
