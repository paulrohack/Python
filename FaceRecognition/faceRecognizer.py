import face_recognition
import cv2
image_file = "FaceRecognition\____.jpg"
k_image = face_recognition.load_image_file(image_file)
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    cv2.imshow("Window", img)
    img = cv2.resize(img,(0,0),None,0.25,0.25)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    k_f = [face_recognition.face_encodings(k_image)[0]]

    u_f = face_recognition.face_encodings(img)
    if u_f != []:
        results = face_recognition.compare_faces(k_f, u_f[0])
        print(results)   

    cv2.waitKey(1)     
