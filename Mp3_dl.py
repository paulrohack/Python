import os
run = True
while run:
    ask = input("[Y]outube or [S]potify Playlist or [Q]uit :")
    if ask.upper() == 'Y':
        url = input("YOUTUBE URL :  ")
        f_url = ("youtube-dl -o G:\Music\DownloadedMusic\%(title)s.%(ext)s -x --audio-format mp3 " + url)
        os.system(f_url)
    elif ask.upper() == 'S':
        url = input("SPOTIFY URL :  ")
        f_url = ("spotify_dl -l " + url + " -o S:\Music")
        os.system(f_url)
    else:
        run = False
