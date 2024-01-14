import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

# Verbindung zur Datenbank herstellen (falls nicht vorhanden, wird eine neue erstellt)
conn = sqlite3.connect('bucketlist.db')
cursor = conn.cursor()

# Tabelle für Ereignisse erstellen, falls sie noch nicht existiert
cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        time TEXT,
        image_path TEXT
    )
''')
conn.commit()

# Tkinter-Fenster erstellen
root = tk.Tk()
root.title("Bucketlist Manager")

# Funktion zum Hinzufügen eines Ereignisses
def add_event():
    title = entry_title.get()
    description = text_description.get("1.0", tk.END).strip()
    time = entry_time.get()

    # Daten in die Datenbank einfügen
    cursor.execute('''
        INSERT INTO events (title, description, time) VALUES (?, ?, ?)
    ''', (title, description, time))
    conn.commit()

    messagebox.showinfo("Erfolg", "Ereignis hinzugefügt")
    clear_entries()

# Funktion zum Anzeigen aller Ereignisse
def show_events():
    cursor.execute('''
        SELECT * FROM events
    ''')
    events = cursor.fetchall()

    for event in events:
        print(event)

# Funktion zum Löschen der Eingabefelder nach dem Hinzufügen eines Ereignisses
def clear_entries():
    entry_title.delete(0, tk.END)
    text_description.delete("1.0", tk.END)
    entry_time.delete(0, tk.END)

# GUI-Elemente erstellen
label_title = tk.Label(root, text="Titel:")
entry_title = tk.Entry(root)

label_description = tk.Label(root, text="Beschreibung:")
text_description = tk.Text(root, height=5, width=30)

label_time = tk.Label(root, text="Zeit:")
entry_time = tk.Entry(root)

button_add = tk.Button(root, text="Ereignis hinzufügen", command=add_event)
button_show = tk.Button(root, text="Alle Ereignisse anzeigen", command=show_events)

# GUI-Elemente platzieren
label_title.grid(row=0, column=0, sticky="w")
entry_title.grid(row=0, column=1, columnspan=2, sticky="w")

label_description.grid(row=1, column=0, sticky="w")
text_description.grid(row=1, column=1, columnspan=2, sticky="w")

label_time.grid(row=2, column=0, sticky="w")
entry_time.grid(row=2, column=1, columnspan=2, sticky="w")

button_add.grid(row=3, column=0, columnspan=3, pady=10)
button_show.grid(row=4, column=0, columnspan=3, pady=10)

# Hauptloop starten
root.mainloop()

# Verbindung zur Datenbank schließen, wenn das Programm beendet wird
conn.close()
