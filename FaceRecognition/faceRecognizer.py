import face_recognition
import cv2

k_image = face_recognition.load_image_file("FaceRecognition\paul.JPG")

cap = cv2.VideoCapture(0)
_, img = cap.read()

k_f = [face_recognition.face_encodings(k_image)[0]]
u_f = face_recognition.face_encodings(img)[0]

results = face_recognition.compare_faces(k_f, u_f)

print(results)        
