from tkinter import *
import tkinter as tk

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    object =TimezoneFinder()
    result=object.timezone_at(lng=location.longitude,lat=location.latitude)
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%m %p \n %d-%m-%Y")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    #weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b080c34d129fb48114a712df81e45381"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)



    
#search Box
Search_image=PhotoImage(file="Images/Search.png.png")
myimage=Label(image=Search_image)
myimage.place(x=650,y=5)


textfield=tk.Entry(root,justify="center",width=22,font=("poppins",10,"bold"),bg="#d8ede9",border=0,fg="black")
textfield.place(x=660,y=98)
textfield.focus()

#Search icon
Search_icon=PhotoImage(file="Images/Search Icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#141414",command=getweather)
myimage_icon.place(x=822,y=95)

#logo
Logo_image=PhotoImage(file="Images/Logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=60)

#Bottom Box
Frame_image=PhotoImage(file="Images/Bottom box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#Label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="White",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="White",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="White",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="White",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)


w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)

p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)


root.mainloop()

    
