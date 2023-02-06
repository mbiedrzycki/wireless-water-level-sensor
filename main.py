import requests
import json
from tkinter import *
import tkinter as tk

#GUI
window = tk.Tk()
window.title('WeatherApp')
city=Label(window,text = "Enter name of the city whose weather you want to know.", font=('Arial',12))
city.grid(row=0)
entry=tk.Entry(window,width=20, font=('Arial',12))
entry.grid(row=1, pady=3)
city_input = entry.get()
entry.focus_set()

def weatherapp():     #api settings
    url = "http://api.openweathermap.org/data/2.5/weather?"
    api = ''
    city_input = entry.get()
    completed_url = url + "appid=" + api + "&q=" + city_input
    response = requests.get(completed_url)
    result = response.json()

    if result['cod'] != '404': #condition for the existence of the city
        #temperature, humidity, pressure
        details = result["main"]
        temperature = details["temp"] - 273.15
        pressure = details["pressure"]
        humidity = details["humidity"]

        #weather description
        weather = result["weather"]
        weather = weather[0]
        description = weather["description"]

        #label weather description
        city_description = str((city_input)+' - ' + description.capitalize())
        label=Label(window, text=city_description,font=('Arial',11), width=25)
        label.grid(row=3)

        info = ("Temperature = "+ str(round(temperature, 2)) + "°C", "Pressure = "+ str(pressure) + "hPa",
              "Humidity = "+ str(humidity) + "%")

        text=Text(window, height = 3, width=25)
        text.grid(row=4,pady=3)

        for x in info:
            text.insert(END, x+'\n')

        entry.delete(0,'end')

    else:  #city doesnt exist
        print("City not found.")

label=Label(window, text="")
label2=Label(window, text="")
label3 = Label(window, text="App created by Michu")
label3.grid(row=5,pady=3)
button = tk.Button(window, text="Enter", command = weatherapp).grid(row=2, pady=3)
window.mainloop()



