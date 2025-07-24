# main.py
import tkinter as tk
from tkinter import messagebox
import cv2
import face_recognition
import sqlite3
import numpy as np

conn = sqlite3.connect('facebase.db')
c = conn.cursor()

def save_user(name, encoding):
    encoding_blob = encoding.tobytes()
    c.execute("INSERT INTO users (name, encoding) VALUES (?, ?)", (name, encoding_blob))
    conn.commit()

def register_user():
    name = name_entry.get()
    if not name:
        messagebox.showerror("Errore", "Inserire un nome")
        return

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        messagebox.showerror("Errore", "Impossibile catturare l'immagine")
        return

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_encodings = face_recognition.face_encodings(rgb_frame)

    if not face_encodings:
        messagebox.showerror("Errore", "Nessun volto rilevato")
        return

    save_user(name, face_encodings[0])
    messagebox.showinfo("Successo", f"Utente {name} registrato")

def recognize_user():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        messagebox.showerror("Errore", "Impossibile catturare l'immagine")
        return

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_encodings = face_recognition.face_encodings(rgb_frame)

    if not face_encodings:
        messagebox.showerror("Errore", "Nessun volto rilevato")
        return

    unknown_encoding = face_encodings[0]
    c.execute("SELECT name, encoding FROM users")
    users = c.fetchall()

    for name, encoding_blob in users:
        known_encoding = np.frombuffer(encoding_blob, dtype=np.float64)
        results = face_recognition.compare_faces([known_encoding], unknown_encoding)

        if results[0]:
            messagebox.showinfo("Riconoscimento", f"Accesso consentito: {name}")
            return

    messagebox.showwarning("Riconoscimento", "Accesso negato")

root = tk.Tk()
root.title("Face Recognition System")

name_entry = tk.Entry(root)
name_entry.pack()

register_btn = tk.Button(root, text="Registra Utente", command=register_user)
register_btn.pack()

recognize_btn = tk.Button(root, text="Riconosci Utente", command=recognize_user)
recognize_btn.pack()

root.mainloop()

