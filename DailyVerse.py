from selenium import webdriver
from PIL import Image
import requests, io, datetime

d = webdriver.Chrome()

d.get('https://www.air1.com/ministry/verse-of-the-day')

img = d.find_element_by_xpath('//*[@id="TodaysVerse"]/div/div[1]/img').get_attribute('src')
d.quit()

response = requests.get(img)
image_bytes = io.BytesIO(response.content)
img = Image.open(image_bytes)
img.show()
t = datetime.date.today()
img.save(f"{t}.png")


