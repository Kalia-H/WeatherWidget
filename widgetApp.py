import tkinter as tk
import requests
import json
with open('api.json','r') as file:
    config = json.load(file)
    api_key = config.get("api_key")
print(f"API Key: {api_key}")
def fetch_weather(event=None):
    root.bind('<Return>', fetch_another)
    city_label.pack_forget()
    city_entry.pack_forget()
    state_label.pack_forget()
    state_entry.pack_forget()
    fetch_button.pack_forget()
    return_home.pack()
    print('width: ',root.winfo_width())
    print('height:',root.winfo_height())
    print('fetch_weather has been clicked')
    city = city_entry.get()
    state = state_entry.get()
    location = f"{city},{state}"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={location}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            celsius = main["temp"]
            description = weather["description"]
            fahrenheit = (celsius * 1.8) + 32
            cap_city = city.capitalize()
            cap_state = state.capitalize()
            print('Temp in Cel : ',celsius,'Temp in Fahren: ',fahrenheit)
            weather_info = f"{cap_city},{cap_state} \n Temperature: {fahrenheit}°F \n Description: {description}"
    else:
        weather_info = f"City Not Found"
    weather_label.config(text=weather_info)

def fetch_another(event=None):
    print('fetch_another pressed')
    root.bind('<Return>', fetch_weather)
    city_label.pack()
    city_entry.pack()
    state_label.pack()
    state_entry.pack()
    fetch_button.pack()
    return_home.pack_forget()

root = tk.Tk()                                                                                                  #Initialize the main window
root.title("Weather Widget")
root.geometry("300x200")                                                                                        #Set the window size
root.config(bg="orange")                                                                                        #Set the bg color to orange                                                                                                                  #create a label for the city input
city_label = tk.Label(root, text="Enter City: ",bg="orange")
city_label.pack()
city_entry = tk.Entry(root, bg="orange")                                                                        #create an entry field for the city
city_entry.pack()
state_label = tk.Label(root, text="Enter State: ",bg="orange")                                                  #create an entry field for the state
state_label.pack()
state_entry = tk.Entry(root,bg="orange")
state_entry.pack()
fetch_button = tk.Button(root, text="Submit", command = fetch_weather, bg="orange",)                            #create a button to fetch the weather
root.bind('<Return>', fetch_weather)
fetch_button.pack()
weather_label = tk.Label(root, text="",bg="orange")                                                        #Placeholder label for displaying weather information
weather_label.pack()
return_home = tk.Button(root, text="Enter new city", bg="orange", command=fetch_another)
root.mainloop()

