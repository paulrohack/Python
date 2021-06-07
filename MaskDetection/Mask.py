import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2

np.set_printoptions(suppress=True)
p = ["Mask", "No Mask"]
nn = 0
pn = 0
n = 0
cap = cv2.VideoCapture(1)
model = tensorflow.keras.models.load_model('H:\Python\AI\MaskDetection\keras_model.h5')
while True:
    _, img = cap.read()
    cv2.imwrite('H:\Python\AI\MaskDetection\img.jpg', img)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open('H:\Python\AI\MaskDetection\img.jpg')
    # image.show()
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.int64) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    nomask = prediction[0,0]
    mask = prediction[0,1]
    maxp = max(mask, nomask)
    pn = n
    if  maxp == mask:
        n = 0
        nn = 0
    else:
        n = 1
        nn = 1
    if pn != nn and int((maxp)*100) > 65:
        print(f'{p[n]}\nConfidenceLevel: {int((maxp)*100)}%')
        


