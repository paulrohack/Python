import selenium
from selenium import webdriver
import time
import tkinter as tk 
window = tk.Tk()


d = webdriver.Chrome()
d.minimize_window()
d.get('https://www.bible.com/verse-of-the-day')
d.implicitly_wait(10)

Title = d.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/h1').text
Date = d.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/amp-date-display/div/p').text
Word = d.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div[1]/p[1]').text
Verse = d.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div[1]/p[2]').text

window.title(Title)
window.geometry('550x175')

tk.Label(window, text=Date.upper() , font = ('Roboto Thin 100', 14, 'bold')).pack()
tk.Label(window, text=Word.upper(),bg = 'light blue', font = ('Roboto thin ', 10), wraplength=500).pack()
tk.Label(window, text=Verse.upper(),bg = 'yellow', font = ('Roboto thin ', 10, 'bold'), wraplength=500).pack()

d.quit()
window.mainloop()