<<<<<<< HEAD
import serial

run = True
try:
    s = serial.Serial('COM5', 9600, timeout=1)
except:
    print('ERROR COMMUNICATING WITH THE BOARD')
    run = False
while run:
    if input() == 'o':
        s.write(b'H')
    if input() == 'f':
=======
import serial

run = True
try:
    s = serial.Serial('COM5', 9600, timeout=1)
except:
    print('ERROR COMMUNICATING WITH THE BOARD')
    run = False
while run:
    if input() == 'o':
        s.write(b'H')
    if input() == 'f':
>>>>>>> 1716e3ac153e6b6805d02dd7397be643a7ac4293
        s.write(b'L')