import sqlite3
conn = sqlite3.connect("../data/fitness.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS workouts")

cur.execute("""
CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_date  TEXT NOT NULL CHECK (workout_date LIKE '____-__-__'),
    workout_type  TEXT NOT NULL,
    workout_duration INTEGER NOT NULL CHECK (workout_duration BETWEEN 1 AND 300),
    workout_notes TEXT DEFAULT 'Keine Notize',
    UNIQUE (workout_date, workout_type)
)
""")

cur.execute(
    "INSERT INTO workouts (workout_date, workout_type, workout_duration) VALUES (?, ?, ?)",

    ("2025-08-27", "Cardio", 20)
)

# cur.execute(
#     "INSERT INTO workouts (workout_date, workout_type, workout_duration) VALUES (?, ?, ?)",
#
#     ("2025-08-27", "Cardio", 40)
# )

##### ------------> ERROR !!! UNIQUE

conn.commit()
conn.close()
