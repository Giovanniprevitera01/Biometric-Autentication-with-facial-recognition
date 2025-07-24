import cv2
import os
import sqlite3
from tkinter import Tk, Label, Button, messagebox
from notifications import send_sms_notification
def recognize_user():

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if not ret:

messagebox.showerror('Error', 'Failed to capture image
')

return

image_path = 'data/current.jpg'

cv2.imwrite(image_path, frame)

cap.release()

os.system(f'br -algorithm FaceRecognition -enroll {
image_path} data/current.csv')

conn = sqlite3.connect('data/face_recognition.db')

c = conn.cursor()

users = c.execute('SELECT name, face_encoding_path FROM
users').fetchall()

best_match = None

best_score = float('inf')

for user in users:

name, face_encoding_path = user

result = os.popen(f'br -algorithm FaceRecognition -
compare {face_encoding_path} data/current.csv').
read()

score = float(result.strip())

if score < best_score:

best_score = score

best_match = name

conn.close()

if best_match and best_score < 0.6:

messagebox.showinfo('Access Granted', fAccess granted
to {best_match})

send_sms_notification('Access granted', f'Access
granted to {best_match}')

else:

messagebox.showinfo('Access Denied', 'Access denied')

send_sms_notification('Access denied', 'Access denied'

)

def main():
root = Tk()

root.title('Recognize User')

Button(root, text='Recognize', command=recognize_user).
pack()

root.mainloop()

if __name__ == '__main__':

main()
