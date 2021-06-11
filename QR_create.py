<<<<<<< HEAD
import qrcode
import os

data = input("Your Data or Link: ")
img = qrcode.make(data)

save = input("Name of The QR-code: ")

dirName = 'Qr_Images'
try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
    img.save(f'Qr_Images/{save}.jpg')
    print("QR saved")
 
except FileExistsError:
    img.save(f'Qr_Images/{save}.jpg')
    print("QR saved")
   
=======
import qrcode
import os

data = input("Your Data or Link: ")
img = qrcode.make(data)

save = input("Name of The QR-code: ")

dirName = 'Qr_Images'
try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
    img.save(f'Qr_Images/{save}.png')
    print("QR saved")
 
except FileExistsError:
    img.save(f'Qr_Images/{save}.png')
    print("QR saved")
   
>>>>>>> 1716e3ac153e6b6805d02dd7397be643a7ac4293
