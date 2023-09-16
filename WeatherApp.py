from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests, json
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#BA55D3")
root.resizable(False, False)


def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # weather
    API_KEY = "864c4318d22ae6d703a6b45f99df272b"
    link = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(link)
    json_data = response.json()

    temp = json_data['list'][0]['main']['temp']
    humidity = json_data['list'][0]['main']['humidity']
    pressure = json_data['list'][0]['main']['pressure']
    wind_speed = json_data['list'][0]['wind']['speed']
    description = json_data['list'][0]['weather'][0]['description']

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind_speed, "m/s"))
    d.config(text=description)

    # first cell
    firstdayimage = json_data['list'][0]['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file=f"Ima/{firstdayimage}.png")
    firstimage.config(image=photo1)
    firstimage.image = photo1

    tempdt1 = json_data['list'][0]['weather'][0]['main']
    temp1 = json_data['list'][0]['main']['temp']
    temphum1 = json_data['list'][0]['main']['humidity']
    day1temp.config(text=f"Description:{tempdt1}\n Temp:{temp1}\n Humidity:{temphum1}")

    # second cell
    seconddayimage = json_data['list'][1]['weather'][0]['icon']
    
    img = (Image.open(f"Ima/{seconddayimage}.png"))
    resized_image = img.resize((60, 60))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempdt2 = json_data['list'][1]['weather'][0]['main']
    temp2 = json_data['list'][1]['main']['temp']
    temphum2 = json_data['list'][1]['main']['humidity']
    day2temp.config(text=f"Description:{tempdt2}\n Temp:{temp2}\n Humidity:{temphum2}")

    # third cell
    thirddayimage = json_data['list'][2]['weather'][0]['main']
    
    img = (Image.open(f"Ima/{thirddayimage}.png"))
    resized_image = img.resize((60, 60))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempdt3 = json_data['list'][2]['weather'][0]['main']
    temp3 = json_data['list'][2]['main']['temp']
    temphum3 = json_data['list'][2]['main']['humidity']
    day3temp.config(text=f"Description:{tempdt3}\n Temp:{temp3}\n Humidity:{temphum3}")

    # fourth cell
    fourthdayimage = json_data['list'][3]['weather'][0]['main']
    
    img = (Image.open(f"Ima/{fourthdayimage}.png"))
    resized_image = img.resize((60, 60))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempdt4 = json_data['list'][3]['weather'][0]['main']
    temp4 = json_data['list'][3]['main']['temp']
    temphum4 = json_data['list'][3]['main']['humidity']
    day4temp.config(text=f"Description:{tempdt4}\n Temp:{temp4}\n Humidity:{temphum4}")
    # fifth cell
    fifthdayimage = json_data['list'][4]['weather'][0]['main']
    
    img = (Image.open(f"Ima/{fifthdayimage}.png"))
    resized_image = img.resize((60, 60))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempdt5 = json_data['list'][4]['weather'][0]['main']
    temp5 = json_data['list'][4]['main']['temp']
    temphum5 = json_data['list'][4]['main']['humidity']
    day5temp.config(text=f"Description:{tempdt5}\n Temp:{temp5}\n Humidity:{temphum5}")

    # sixth cell
    sixthdayimage = json_data['list'][5]['weather'][0]['main']
    
    img = (Image.open(f"Ima/{sixthdayimage}.png"))
    resized_image = img.resize((60, 60))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempdt6 = json_data['list'][5]['weather'][0]['main']
    temp6 = json_data['list'][5]['main']['temp']
    temphum6 = json_data['list'][5]['main']['humidity']
    day6temp.config(text=f"Description:{tempdt6}\n Temp:{temp6}\n Humidity:{temphum6}")

    # seventh cell
    seventhdayimage = json_data['list'][6]['weather'][0]['main']
    
    img = (Image.open(f"Ima/{seventhdayimage}.png"))
    resized_image = img.resize((60, 60))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7

    tempdt7 = json_data['list'][6]['weather'][0]['main']
    temp7 = json_data['list'][6]['main']['temp']
    temphum7 = json_data['list'][6]['main']['humidity']
    day7temp.config(text=f"Description:{tempdt7}\n Temp:{temp7}\n Humidity:{temphum7}")

    # days
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


##iconos
image_icon = PhotoImage(file="Ima/logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="Ima/Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#BA55D3",).place(x=40, y=110)

# label
label1 = Label(root, text="Temperature", font=('Helvetica',11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=('Helvetica', 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure", font=('Helvetica', 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed", font=('Helvetica', 11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=('Helvetica', 11), fg="white", bg="#203243")
label5.place(x=50, y=200)

# search_box
Search_image = PhotoImage(file="Ima/Rounded Rectangle 3.png")
myimage = Label(image=Search_image, bg="#BA55D3")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file="Ima/Layer 7.png")
weatherimage = Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=290, y=127)

textfield = tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=370, y=130)
textfield.focus()

Search_icon = PhotoImage(file="Ima/Layer 6.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command= getWeather)
myimage_icon.place(x=645, y=125)

# Bottom box
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# bottom boxes
firstbox = PhotoImage(file="Ima/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Ima/Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=900, y=30)

# clock (here we will place time)
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#BA55D3")
clock.place(x=30, y=20)

# timezone
timezone = Label(root, font=("Helvetica", 12), fg="white", bg="#BA55D3")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Helvetica", 12), fg="white", bg="#BA55D3")
long_lat.place(x=700, y=50)

# thpwd
t = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=150, y=120)
h = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=150, y=140)
p = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=150, y=160)
w = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=150, y=180)
d = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=150, y=200)

# first cell
firstframe = Frame(root, width=230, height=132, bg="#282829")
firstframe.place(x=35, y=315)

day1 = Label(firstframe, font="Arial 16", bg="#282829", fg="#fff")
day1.place(x=110, y=5)
firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=1, y=15)
day1temp = Label(firstframe, bg="#282829", fg="#57adff", font="arial 11 bold")
day1temp.place(x=100, y=50)

# second cell
secondframe = Frame(root, width=70, height=115, bg="#282829")
secondframe.place(x=305, y=325)

day2 = Label(secondframe, bg="#282829", fg="#fff")
day2.place(x=10, y=5)
secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=7, y=20)
day2temp = Label(secondframe, bg="#282829", fg="#57adff", font="arial 6 bold")
day2temp.place(x=1, y=70)

# third cell
thirdframe = Frame(root, width=70, height=115, bg="#282829")
thirdframe.place(x=405, y=325)

day3 = Label(thirdframe, bg="#282829", fg="#fff")
day3.place(x=12, y=5)
thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=7, y=20)
day3temp = Label(thirdframe, bg="#282829", fg="#57adff",font="arial 6 bold")
day3temp.place(x=0, y=70)

# fouth cell
fourthframe = Frame(root, width=70, height=115, bg="#282829")
fourthframe.place(x=505, y=325)

day4 = Label(fourthframe, bg="#282829", fg="#fff")
day4.place(x=10, y=5)
fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=7, y=20)
day4temp = Label(fourthframe, bg="#282829", fg="#57adff", font="arial 6 bold")
day4temp.place(x=0, y=70)

# fifth cell
fifthframe = Frame(root, width=70, height=115, bg="#282829")
fifthframe.place(x=605, y=325)

day5 = Label(fifthframe, bg="#282829", fg="#fff")
day5.place(x=10, y=5)
fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=7, y=20)
day5temp = Label(fifthframe, bg="#282829", fg="#57adff",font="arial 6 bold")
day5temp.place(x=0, y=70)

# sixth cell
sixthframe = Frame(root, width=70, height=115, bg="#282829")
sixthframe.place(x=705, y=325)

day6 = Label(sixthframe, bg="#282829", fg="#fff")
day6.place(x=10, y=5)
sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=7, y=20)
day6temp = Label(sixthframe, bg="#282829", fg="#57adff", font="arial 6 bold")
day6temp.place(x=0, y=70)

# seventh cell
seventhframe = Frame(root, width=70, height=115, bg="#282829")
seventhframe.place(x=805, y=325)

day7 = Label(seventhframe, bg="#282829", fg="#fff")
day7.place(x=10, y=5)
seventhimage = Label(seventhframe, bg="#282829")
seventhimage.place(x=7, y=20)
day7temp = Label(seventhframe, bg="#282829", fg="#57adff",font="arial 6 bold")
day7temp.place(x=0, y=70)

root.mainloop()
