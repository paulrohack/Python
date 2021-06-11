<<<<<<< HEAD
import os

run = True

path = 'G:\Music\DownloadedMusic'
try:
    os.mkdir(path)
except FileExistsError:
    print("Path already exists")

while run:
    ask = input("[Y]outube or [Q]uit :")
    if ask.upper() == 'Y':
        url = input("YOUTUBE URL :  ")
        f_url = ("youtube-dl -o G:\Music\DownloadedMusic\%(title)s.%(ext)s -x --audio-format mp3 " + url)
        os.system(f_url)
    else:
        run = False

=======
import os

run = True

path = 'G:\Music\DownloadedMusic'
try:
    os.mkdir(path)
except FileExistsError:
    print("Path already exists")

while run:
    ask = input("[Y]outube or [Q]uit :")
    if ask.upper() == 'Y':
        url = input("YOUTUBE URL :  ")
        f_url = ("youtube-dl -o G:\Music\DownloadedMusic\%(title)s.%(ext)s -x --audio-format mp3 " + url)
        os.system(f_url)
    else:
        run = False

>>>>>>> 1716e3ac153e6b6805d02dd7397be643a7ac4293
