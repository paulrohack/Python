from tkinter import *
import webbrowser
import subprocess
root = Tk()
mailpath = 'GUI\MAIL.png'
mapspath = 'GUI\MAPS.png'
youtubepath = 'GUI\YOUTUBE.png'
googlepath = 'GUI\GOOGLE.png'

root.geometry('690x400')
root.wm_title("SEARCH OPEN")
Label(root,text= "SEARCH"  , font = ('algerian',30,'bold','underline')).pack()

Canvas(root,height = 50,width = 50).pack()
TextVar = StringVar()
textbox = Entry(textvariable=TextVar,width = 200, bg = 'light blue',bd=10, font = ('ariel')).pack()

MAIL = PhotoImage(file = mailpath)
GOOGLE = PhotoImage(file = googlepath)
MAPS = PhotoImage(file = mapspath)
YOUTUBE = PhotoImage(file = youtubepath)

def clear():                                                                 
    abc =  ''
    TextVar.set(abc) 

def MapsText():
    a = TextVar.get()
    if a != '':
        webbrowser.open_new("https://www.google.com/maps/search/" + a +'/@13.0498258,77.6388008,13z/data=!3m1!4b1')
    else:
        webbrowser.open_new("https://www.google.com/maps/@13.0497285,77.6650655,15z")
    clear()

def GoogleText():
    b = TextVar.get()
    if b != '':
        webbrowser.open_new("https://www.google.com/search?q=" + b)
    else:
        webbrowser.open_new("https://www.google.com/")
    clear()
    
def YoutubeText():
    c = TextVar.get()
    if c != '':
        webbrowser.open_new("https://www.youtube.com/results?q=" + c)
    else:
        webbrowser.open_new("https://www.youtube.com/")
    clear()
        
def Mail():
    d = TextVar.get()
    if d == '':
        webbrowser.open_new('https://mail.google.com/mail/u/0')
    else:
        webbrowser.open_new('https://mail.google.com/mail/u/0/#advanced-search/exclude_chats=true&query=' + d + '&isrefinement=true')
    clear()


Button(root,padx = 50, pady = 10,image = GOOGLE, command = GoogleText,  bg = 'green',bd = 10).pack(side = LEFT)
Button(root,padx = 30, pady = 10,image = YOUTUBE,command = YoutubeText,  bg = 'red', bd = 10).pack(side = LEFT)
Button(root, padx=30, pady=10,image = MAPS, command= MapsText,  bg = 'yellow', bd = 10).pack(side = LEFT)
Button(root, padx =30, pady = 10, image = MAIL, command = Mail,  bg = 'white',bd = 10).pack(side = LEFT)

root.mainloop()


