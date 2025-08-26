## Datenbankverbindung
- Bei SQLite ist die Datenbank nur eine Datei (z.B. fitness.db).
- Mit Python öffnen wir diese Datei mit dem Modul sqlite3.

## Begriff Verbindung (connection):

- Das ist die "Leitung" von deinem Python-Programm zur Datenbankdatei.

- Solange die Verbindung offen ist, kannst du Befehle schicken (z.B. „Erstelle Tabelle“).

- Am Ende schließt du die Verbindung wieder, damit nichts kaputt geht.

## Verbindung öffnen

````python
import sqlite3

# Verbindung herstellen (öffnet oder erstellt die Datei fitness.db)
conn = sqlite3.connect("fitness.db")

# Verbindung wieder schließen
conn.close()
````
#### Erklärungen:

- import sqlite3: damit holst du dir das eingebaute Python-Modul.

- sqlite3.connect("fitness.db"): öffnet die Datei fitness.db. Wenn sie noch nicht existiert, wird sie erstellt.

- conn ist jetzt dein „Kabel“ zur Datenbank.

- conn.close(): kappt die Leitung wieder. Immer wichtig, wenn du fertig bist.


## Was ist ein Cursor
- Wenn die Verbindung wie ein Kabel ist, dann ist der Cursor der „Stift“, mit dem du Befehle in die Datenbank schreibst.

- Mit der Verbindung conn kannst du einen Cursor erzeugen.

- Über den Cursor schickst du SQL-Befehle (z.B. CREATE TABLE, INSERT, SELECT).

- Ohne Cursor keine Kommunikation.

````python
import sqlite3

conn = sqlite3.connect("fitness.db")

cur = conn.cursor()

conn.close()
````
#### Erklärung:

- cur = conn.cursor() bedeutet: Gib mir ein Werkzeug, mit dem ich SQL schreiben darf.

- Der Cursor „merkt sich“ auch, welches Ergebnis zuletzt kam.


## Datentypen SQlite
- INTEGER für ganze Zahlen, z.B. Minuten

- REAL für Kommazahlen, z.B. Gewicht 72.5

- TEXT für Texte, z.B. Notizen, Kategorien

- NULL bedeutet „kein Wert hinterlegt“

- Tipp: Für Datum starten wir pragmatisch mit TEXT im Format YYYY-MM-DD wie 2025-08-26. Das ist gut sortierbar und leicht zu lesen.

## Wichtige Constraints, leicht erklärt

- Constraints sind Regeln, die die Datenqualität schützen.

PRIMARY KEY
- Eine eindeutige Kennung jeder Zeile. In SQLite ist INTEGER PRIMARY KEY besonders: die Datenbank vergibt automatisch fortlaufende Zahlen.

NOT NULL
- Diese Spalte darf nie leer sein. Beispiel: Ein Workout ohne Datum wäre sinnlos.

UNIQUE
- Werte dürfen sich nicht wiederholen. Beispiel wäre ISBN in einer Bücherliste. Für Workouts oft nicht nötig.

CHECK (Bedingung)
- Zusätzliche Regel. Beispiel: duration_min > 0 verhindert negative Dauer.

DEFAULT Wert
- Standardwert, wenn du keinen angibst. Beispiel: DEFAULT '' für leere Notizen. Ich empfehle bei notes eher kein Default und erlaube NULL.