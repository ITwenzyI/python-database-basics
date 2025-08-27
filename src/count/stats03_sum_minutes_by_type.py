import sqlite3
conn = sqlite3.connect("../../data/fitness.db")
cur = conn.cursor()


# Wie viele Minuten habe ich pro Typ trainiert?
cur.execute("""
SELECT workout_type, SUM(workout_duration) FROM workouts GROUP BY workout_type
""")
for wtype, total_min in cur.fetchall():
    print(f"{wtype}: {total_min} Minuten insgesamt.")

cur.execute("""
SELECT workout_type, MAX(workout_duration) FROM workouts GROUP BY workout_type
""")
for wtype, total_min in cur.fetchall():
    print(f"{wtype}: {total_min} Minuten maximal.")

cur.execute("""
SELECT workout_type, MIN(workout_duration) FROM workouts GROUP BY workout_type
""")
for wtype, total_min in cur.fetchall():
    print(f"{wtype}: {total_min} Minuten minimal.")

cur.execute("""
SELECT workout_type, AVG(workout_duration) FROM workouts GROUP BY workout_type
""")
for wtype, total_min in cur.fetchall():
    print(f"{wtype}: {total_min} Minuten durchschnittlich.")

cur.execute("""
SELECT workout_type, COUNT(workout_duration) FROM workouts GROUP BY workout_type
""")
for wtype, total_min in cur.fetchall():
    print(f"{wtype}: {total_min} Einheiten insgesamt.")



conn.commit()
conn.close()
