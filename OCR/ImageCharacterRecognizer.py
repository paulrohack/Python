import pytesseract
import cv2
from PIL import Image
from googletrans import Translator
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\paulr\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

# cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
path = 'H:\Python\OCR\Image.jpg'
img = cv2.imread(path) 
# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
translator = Translator()
t = []
l = True
while True:

    cv2.imshow('OCR', img)
    word = pytesseract.image_to_data(Image.open(path))
    word = word.splitlines()
    if l:
        for e, i in enumerate(word):
            if e != 0:
                i = i.split()
                x, y, w, h = (int(i[6]), int(i[7]), int(i[8]), int(i[9]))
                if len(i) == 12:
                    text = i[11]
                    translated = translator.translate(text, dest='english')
                    t.append((translated.text).upper())
                    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB) 
                    cv2.rectangle(img,(x, y), (x+w, y+h) , (255, 0, 0))
                    # cv2.putText(img, translated.text, (x, y), font, 0.5, (0, 0, 255), 2) 
            if e == len(word)-1:
                t = str(t).replace(', ', ' ').replace("'", '')
                if t == '[]':
                    print("NOTHING RECOGNIZED")
                    
                else:
                    print("RECOGNIZED : " + t)
                l = False           
    if cv2.waitKey(1) & 0xff == ord('q'):     
        break