import os

run = True

path = 'G:\Music\DownloadedMusic'
try:
    os.mkdir(path)
except FileExistsError:
    # print("Path already exists")
    pass
while run:
    ask = input("[Y]outube or [Q]uit :")
    if ask.upper() == 'Y':
        url = input("YOUTUBE URL :  ")
        f_url = ("youtube-dl -o G:\Music\DownloadedMusic\%(title)s.%(ext)s -x --audio-format mp3 " + url)
        os.system(f_url)
    else:
        run = False

