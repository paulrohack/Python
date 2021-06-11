import cv2

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    cv2.imshow("ROI selector", img)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        box = cv2.selectROI(img, False)
        cv2.destroyWindow('ROI selector')
        break

tracker = cv2.TrackerKCF_create()
tracker.init(img, box)

run = True
while run:
    _, img = cap.read()
    working, box = tracker.update(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        run = False
    if working:
        #    print(box)
           x, y = (int(box[0]), int(box[1]))
           w, h = (int(box[0] + box[2]), int(box[1] + box[3]))
           cv2.rectangle(img, (x, y), (w, h), (0,0,255), 2, 1)

    else :
        cv2.putText(img, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    cv2.imshow("window", img)
