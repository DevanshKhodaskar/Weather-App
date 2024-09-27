import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import weatherAPI
import wallpaper

# Initialize the Tkinter window
window = tk.Tk()

window.title("Weather App")
window.wm_iconbitmap("Weather App/Resources/app icon.ico")



# Set the background image
background_image = Image.open(wallpaper.setWallpaper())
image_width, image_height = background_image.size
tk_image = ImageTk.PhotoImage(background_image)

canvas = tk.Canvas(window, width=image_width, height=image_height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
    
# Set window size and prevent resizing
window.geometry('600x700+0+0')
window.resizable(False, False)

# Create canvas text for weather data and welcome message
weather_text = canvas.create_text(275, 275, text='', font=('times new roman', 15), fill='white')
canvas.create_text(300, 70, text='Welcome, Please Enter the Name Of the City', font=('Helvetica', 20), fill='white')

#search bar image
# searchBar=tk.PhotoImage(file="C:/Users/ACER/OneDrive/Desktop/my coding/python/TKinter/10000Project!/Resources/searchBar.png")
# searchBarIcon=tk.Label(image=searchBar)
# searchBarIcon.place(x=60,y=110)

# Input text box
inputText = tk.Entry(window,justify='center', width=30, font=('arial', 12), relief='flat', border=4)
inputText.place(x=150, y=110)

# Create Data Output Drwaings
tempDisplay=canvas.create_text(150,400,text='',font=('helvetica',25),fill="White")
humidityDisplay=canvas.create_text(510,390,text='',font=('helvetica',25),fill="White")
uvDisplay = canvas.create_text(165,580,text='',font=('helvetica',28),fill="White")
windDisplay=canvas.create_text(540,580,text='',font=('helvetica',25),fill="White")
# Global variables to hold PhotoImage references
temp_photo = None
humidity_photo = None
wind_photo = None
uv_photo = None

def click():
    global temp_photo, humidity_photo, wind_photo, uv_photo

    city = inputText.get()

    try:
        # Load and display images
        temp_path = "Weather App/Resources/tempLogo2.png"
        tempimage = Image.open(temp_path)
        temp_photo = ImageTk.PhotoImage(tempimage)
        canvas.create_image(20, 350, image=temp_photo, anchor=tk.NW)

        humidity_path = "Weather App/Resources/icons8-humidity-96.png"
        humidityimage = Image.open(humidity_path)
        humidity_photo = ImageTk.PhotoImage(humidityimage)
        canvas.create_image(400, 340, image=humidity_photo, anchor=tk.NW)

        wind_path = "Weather App/Resources/icons8-wind-96.png"
        windimage = Image.open(wind_path)
        wind_photo = ImageTk.PhotoImage(windimage)
        canvas.create_image(385, 530, image=wind_photo, anchor=tk.NW)

        uv_path = "Weather App/Resources/icons8-uv-index-64.png"
        uvimage = Image.open(uv_path)
        uv_photo = ImageTk.PhotoImage(uvimage)
        canvas.create_image(20, 530, image=uv_photo, anchor=tk.NW)

        # Fetch weather data
        tempData,humidityData,windData,uvData = weatherAPI.weather(city)
        # set Global Variable
        canvas.itemconfig(tempDisplay,text=tempData)
        canvas.itemconfig(humidityDisplay,text=humidityData)
        canvas.itemconfig(uvDisplay,text=str(uvData))
        canvas.itemconfig(windDisplay,text=windData)

        

    except Exception as e:
        if city == '':
            messagebox.showerror("Error", "Please enter a proper City Name")
        else:
            messagebox.showerror("Error", f"Failed to fetch weather data: {str(e)}")

# Button to trigger the click function
button = tk.Button(canvas, text="Check", font=('Arial', 15), bg='white',cursor='hand2',command=click)
button.place(x=260, y=170)

# Run the Tkinter main loop
window.mainloop()
