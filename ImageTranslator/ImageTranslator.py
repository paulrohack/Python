import pytesseract
import cv2
from PIL import Image
from googletrans import Translator
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\paulr\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

cap = cv2.VideoCapture()
translator = Translator()

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    _, img = cap.read()  
    cv2.imshow('s', img)
    if cv2.waitKey(1) & 0xff == ord('w'):
        print("Taken pic") 
        cv2.destroyWindow('s')
        cv2.imwrite('H:\Python\ImageTranslator\img.png', img)
        word = pytesseract.image_to_data(Image.open('H:\Python\ImageTranslator\img.png'))
        word = word.splitlines()
        for e, i in enumerate(word):
            if e != 0:
                i = (i.split())
                
                x, y, w, h = (int(i[6]), int(i[7]), int(i[8]), int(i[9]))
                if len(i) == 12:
                    c = i[11]

                    t = translator.translate(c, dest='english')
                    cv2.rectangle(img,(x, y), (x+w, y+h) , (255, 0, 0))
                    cv2.putText(img, t.text, (x, y - h), font, 0.5, (0, 0, 255), 2)
                    
                    cv2.imwrite('H:\Python\ImageTranslator\img.png', img)
        i = Image.open('H:\Python\ImageTranslator\img.png')
        i.show()
    if cv2.waitKey(1) & 0xff == ord('q'):        
        break