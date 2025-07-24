import cv2
import os
 import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox
def register_user(name):

if not name:

messagebox.showerror(Error, 'Name cannot be empty')

return

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if not ret:

messagebox.showerror('Error', 'Failed to capture image
')

return

image_path = f'data/{name}.jpg'

cv2.imwrite(image_path, frame)

cap.release()

os.system(f'br -algorithm FaceRecognition -enroll {
image_path} data/{name}.csv')

conn = sqlite3.connect('data/face_recognition.db')

c = conn.cursor()

c.execute('INSERT INTO users (name, face_encoding_path)
VALUES (?, ?)', (name, f'data/{name}.csv'))

conn.commit()

conn.close()

messagebox.showinfo('Success', 'User registered
successfully')
def main():

root = Tk()

root.title('Register User')

Label(root, text='Name:').grid(row=0, column=0)

name_entry = Entry(root)

name_entry.grid(row=0, column=1)

Button(root, text='Register', command=lambda:
register_user(name_entry.get())).grid(row=1,
columnspan=2)

root.mainloop()
if __name__ == '__main__':

main()
