from tkinter import *
import webbrowser
import subprocess
root = Tk()
path = 'D://Projects//My_Projects_All//Projects-Python-master//SEARCH//'

root.geometry('690x400')
root.wm_title("OPEN EASY")
Label(root,text= "Search"  , font = ('algerian',30,'bold','underline')).pack()

Canvas(root,height = 50,width = 50).pack()
TextVar = StringVar()
Entry(textvariable=TextVar,width = 200, bg = 'light blue',bd=10, font = ('ariel')).pack()

MAIL = PhotoImage(file = path + "MAIL.png")
GOOGLE = PhotoImage(file = path + "GOOGLE.png")
MAPS = PhotoImage(file = path + "MAPS.png")
YOUTUBE = PhotoImage(file = path + "YOUTUBE.png")



def MapsText():
    a = TextVar.get()
    webbrowser.open_new("https://www.google.com/maps/place/" + a +'/@16.9872867,81.7363176,12z')
def GoogleText():
    b = TextVar.get()
    webbrowser.open_new("https://www.google.com/search?q=" + b)
def YoutubeText():
    c = TextVar.get()
    webbrowser.open_new("https://www.youtube.com/results?q=" + c)
def Mail():
    webbrowser.open_new('https://mail.google.com/mail/u/0/')

Button(root,padx = 50, pady = 10,image = GOOGLE, command = GoogleText,  bg = 'green',bd = 10).pack(side = LEFT)
Button(root,padx = 30, pady = 10,image = YOUTUBE,command = YoutubeText,  bg = 'red', bd = 10).pack(side = LEFT)
Button(root, padx=30, pady=10,image = MAPS, command= MapsText,  bg = 'yellow', bd = 10).pack(side = LEFT)
Button(root, padx =30, pady = 10, image = MAIL, command = Mail,  bg = 'white',bd = 10).pack(side = LEFT)

root.mainloop()


