# WeatherWidget
A simple weather desktop widget

Overview
This is a Python-based GUI application that fetches real-time weather data using the OpenWeather API. The app allows users to enter a city and state, retrieve weather conditions, and display temperature in Fahrenheit.

Features
✅ Graphical User Interface (GUI) built with Tkinter
✅ Fetches live weather data using the OpenWeather API
✅ Displays temperature in Fahrenheit and a weather description
✅ Handles user input for city and state
✅ Simple and lightweight, ideal for quick weather checks

Requirements
Before running the application, ensure you have the following installed:
✅ Python 3.x
✅ requests library(pip install requests)
✅ OpenWeather API key (stored in api.json)

Installation & Setup
✅ Clone the repository
git clone https://github.com/Kalia-H/weather-widget.git
cd weather-widget
✅ Install dependencies
pip install -r requirements.txt
✅Add OpenWeather API Key
  *Create api.json in the project directory
  *Inside api.json, store your API key like this
  {
    "api_key": "YOUR_API_KEY"
  }
  
Run the application
python weather_widget.py



