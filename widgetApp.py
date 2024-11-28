import tkinter as tk
import sys
import requests
print(sys.executable)
print(sys.path)
root = tk.Tk()
#create a globally accessable button to fetch the weather
city_entry = tk.Entry(root)
def fetch_weather():
    print('fetch_weather has been clicked')
    api_key = "e9b0c39801a4babcbc72d44395caa093"
    city = city_entry.get()
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        celsius = main["temp"]
        description = weather["description"]
        fahrenheit = (celsius * 1.8) + 32
        print('Temp in Cel : ',celsius,'Temp in Fahren: ',fahrenheit)
        weather_info = f"Temperature in this bitch: {fahrenheit}°F \n Description: {description}"
    else:
        weather_info = f"City Not Found"
    weather_label.config(text=weather_info)#Initialize the main window
def getWeather():
    #hide the get weather widget
    weather_button.pack_forget()
    #create a label for the city input
    city_label = tk.Label(root, text="Enter City: ")
    city_label.pack()
    city_label.config(bg="orange")
    city_entry.pack()
    city_entry.config(bg="orange")
    #create a button to fetch the weather
    fetch_button = tk.Button(root, text="Submit", command = fetch_weather)
    fetch_button.pack()
    fetch_button.config(bg="orange")
    #Placeholder label for displaying weather information
    weather_label = tk.Label(root, text="Hello")
    weather_label.pack()
    weather_label.config(bg="orange")
    
root.title("Weather Widget")
#Set the window size
root.geometry("300x200")
#Set the bg color to orange
root.config(bg="orange")
weather_button = tk.Button(root, text="Get weather", command = getWeather)
weather_button.pack()
root.mainloop()

