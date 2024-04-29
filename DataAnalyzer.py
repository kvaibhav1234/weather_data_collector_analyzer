
import requests 

class DataAnalyzer:

    """

    DataAnalyzer.py 

    - Used to analyze data from the OpenWeatherMap API. 
    
    """

    def __init__(self, transformed_data):
        self.transformed_data = transformed_data

    #Calculation to find what the average temperature is. 
    def average_temperature(self):
        return self.transformed_data['temperature']

    #Calculation to find what the wind speed is. 
    def max_wind_speed(self):
        # Calculate max wind speed
        return self.transformed_data['wind_speed']

     #Calculation to find what the humidity is. 
    def humidity(self):
        # Calculate humidity
        return self.transformed_data['humidity']

"""

DataRetriever: 

- Used to retrieve data from the OpenWeatherMap API and used to help the DataAnalyzer class. 

"""

class DataRetriever:
    #Method initializes DataRetriever object. 
    def __init__(self, api_key):
        self.api_key = api_key
    
    #Method creates a request URL and sends HTTP GET request to API and returns weather data in dictionary format.
    def get_weather_data(self, city_name):
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = { #Dictionary to contain parameters passed in HTTP GET request. 
            "q": city_name, #Name of city requested. 
            "appid": self.api_key, #API key required by OpenWeatherMap API. 
            "units": "metric"  #Metric units --> unit that is globally used. 
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200: #Indicates request is successful. 
            return response.json()  # Return the weather data dictionary directly.
        else:
            print("Error:", response.status_code)
            return None

#Only executed when script is run directly --> when individual class needs to be tested. 
if __name__ == "__main__":
    api_key = '37dfd4a9fb16f671fbc8618ed078efed'
    city_name = input("Enter name of a city: ")

    retriever = DataRetriever(api_key)
    weather_data = retriever.get_weather_data(city_name)

    if weather_data:

        analyzer = DataAnalyzer(weather_data)

        print("-----------> DATA ANALYZER CLASS RESULTS: ")

        average_temp = analyzer.average_temperature()
        print("Average temperature:", average_temp, "°C") 

        max_wind = analyzer.max_wind_speed()
        print("Max wind speed:", max_wind, "m/s")

        humidity = analyzer.humidity()
        print("Humidity:", humidity, "g/kg")

        feels_like = analyzer.feels_like()
        print("Feels Like:", feels_like, "°C")

        pressure = analyzer.pressure()
        print("Pressure:", pressure, "Pa")
    
    else:
        print("Failed to retrieve weather data.")