from tkinter import *
import requests
from bs4 import BeautifulSoup

print("..........Weather Report..........")
print("..........Weather Report..........")

city = str(input("ENTER YOUR CITY : "))

url=f"https://www.google.com/search?q=weather+in+"+city+"&oq=w&aqs=chrome.2.69i60j69i59l2j69i60l4.1814j1j7&sourceid=chrome&ie=UTF-8"

r=requests.get(url)

s=BeautifulSoup(r.text, "html.parser")

update = s.find("div", class_="BNeawe").text

print(update)