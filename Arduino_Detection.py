import cvzone
import cv2
import serial, time
run = True
try:
    s = serial.Serial('COM5', 9600, timeout=1)
except:
    print("ERROR COMMUNICATION WITH BOARD")
    run = False
    
if run:
    cap = cv2.VideoCapture(0)
    detector = cvzone.PoseDetector()

while run:
    success, img = cap.read()
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img)
    if (lmList[0]) != []:
        s.write(b'H')
        # text = f"Intruder_Found_at_{round(time.time())}"
        # print(text)
        # cv2.imwrite(f'H:\Python\Images\{text}.jpg', img)
    else:
        s.write(b'L')
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xff == ord('q'):        
        run = False
