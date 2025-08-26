import sqlite3

conn = sqlite3.connect('../data/fitness.db')

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS workouts")

cur.execute("""
CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_date TEXT NOT NULL CHECK(workout_date LIKE '____-__-__'),
    workout_type TEXT NOT NULL CHECK (workout_type IN ('Beine', 'Oberkoerper', 'Cardio')),
    workout_duration INTEGER NOT NULL CHECK (workout_duration BETWEEN 01 AND 300),
    workout_notes TEXT
)
""")


conn.commit()

conn.close()