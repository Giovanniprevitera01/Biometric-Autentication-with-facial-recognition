import sqlite3
import os

def create_tables():
os.makedirs('data', exist_ok=True)

conn = sqlite3.connect('data/face_recognition.db')

c = conn.cursor()

c.execute(’’'CREATE TABLE IF NOT EXISTS users (

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT NOT NULL,

face_encoding_path TEXT NOT NULL,

accesses INTEGER DEFAULT 0

)’’')

c.execute(’’'CREATE TABLE IF NOT EXISTS access_log (

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT NOT NULL,

access_granted BOOLEAN NOT NULL,

timestamp DATETIME DEFAULT
CURRENT_TIMESTAMP

)’’')

conn.commit()

conn.close()

if __name__ == '__main__':
create_tables()
