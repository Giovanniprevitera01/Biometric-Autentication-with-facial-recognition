from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

def get_db_connection():
conn = sqlite3.connect('data/face_recognition.db')

conn.row_factory = sqlite3.Row

return conn



@app.route('/api/logs', methods=['GET'])
def get_logs():

conn = get_db_connection()


logs = conn.execute('SELECT * FROM access_log').fetchall()
conn.close()
return jsonify([dict(log) for log in logs])

@app.route('/api/users', methods=['GET'])
def get_users():

conn = get_db_connection()

users = conn.execute('SELECT * FROM users').fetchall()

conn.close()

return jsonify([dict(user) for user in users])

@app.route('/api/logs', methods=['POST'])
def add_log():

data = request.json

name = data['name']

access_granted = data['access_granted']

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

conn = get_db_connection()
conn.execute('INSERT INTO access_log (name, access_granted
, timestamp) VALUES (?, ?, ?)',
(name, access_granted, timestamp))
conn.commit()
conn.close()
return jsonify({'status': 'success'})

@app.route('/api/users/<name>/increment_accesses', methods=['
POST'])
def increment_accesses(name):

conn = get_db_connection()

conn.execute('UPDATE users SET accesses = accesses + 1
WHERE name = ?', (name,))
conn.commit()

conn.close()

return jsonify({'status': 'success'})

if __name__ == '__main__':
app.run(debug=True)
