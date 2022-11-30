import requests
import tkinter as tk
from tkinter import messagebox
from io import BytesIO
from PIL import Image, ImageTk


def get_weather():
    print("Введите название города")
    city_name = input()
    weather_key = "69567d896e8880df9ef919e8a9f097c8"
    try:
        weather_request = requests.get(
            'https://api.openweathermap.org/data/2.5/weather',
            params={'q':city_name, 'appid': weather_key, 'units': 'metric', 'lang': 'ru'})
        json_weather = weather_request.json()
        description = json_weather.get('weather')[0].get('description')
        temp = json_weather.get('main').get('temp')
        wind = json_weather.get('wind').get('speed')
        print("Выбранный город: " + city_name)
        print("Текущая погода - %s, %.1f°C. Скорость ветра %.1f м/с" % (description, temp, wind))
    except Exception:
        print("Не удалось получить ответ. Попробовать еше раз? (y/n)")
        if input() == 'y':
            get_weather()
    print("Еще один город? (y/n)")
    if input() == 'y':
        get_weather()

def find_ISS():
    try:
        iss_url = "http://api.open-notify.org/iss-now.json"
        iss_request = requests.get(iss_url)
        iss_json = iss_request.json()
        lon = iss_json.get("iss_position").get("longitude")
        lat = iss_json.get("iss_position").get("latitude")
        print("Текущее положение МКС")
        print("Широта: %s" % (lat))
        print("Долгота: %s" % (lon))
    except Exception:
        print("Не удалось найти МКС")

def astros():
    try:
        astros_url = "http://api.open-notify.org/astros.json"
        astros_request = requests.get(astros_url)
        astros_json = astros_request.json()
        for i in astros_json.get("people"):
            print("Имя: %s, космический аппарат: %s" % (i.get("name"), i.get('craft')))
        print("Всего человек в космосе: %s" % (astros_json.get("number")))
    except Exception:
        print("Не удалось посчитать космонавтов")


def try_requests():
    try:
        r = requests.get("http://open-notify.org")
        print(r)
    except Exception:
        print("Что-то пошло не так")

def get_kitten():
   url = 'https://aws.random.cat/meow'
   try:
       cats_request = requests.get(url)
       pic_url = cats_request.json().get('file')
       pic_res = requests.get(pic_url)
       buffer = open("Buffer", 'wb')
       buffer.write(pic_res.content)
       buffer.close()
       img = Image.open("Buffer")
       img = img.resize((500, 500), Image.Resampling.LANCZOS)
       image = ImageTk.PhotoImage(img)
       label.config(image=image)
       label.image = image
       img.close()
   except Exception:
       messagebox.showerror("Ошибка", "Не удалось установить соединение")




print("Приветствую!")
print("Показать результат первого задания? (y/n)")
if input()=='y':
    try_requests()
print("Показать результат второго задания? (y/n)")
if input()=='y':
    get_weather()
print("Показать результат третьего задания? (y/n)")
if input()=='y':
    astros()
    find_ISS()
print("Показать результат дополнительного задания? (y/n)")
if input()=='y':
    root = tk.Tk()
    icon = tk.PhotoImage(file='cat-logo.png')
    root.title('Cat Generator')
    root.resizable(False, False)
    root.iconphoto(False, icon)

    img = Image.open("MyCat.jpg")
    img = img.resize((500, 500), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=image)
    label.pack(side="top", fill="both", expand="no")
    tk.Button(root, text='Moar!', command=get_kitten).place(x=240, y=245)
    root.mainloop()



