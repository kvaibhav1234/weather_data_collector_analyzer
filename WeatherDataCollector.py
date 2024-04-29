
import requests

"""

WeatherDataCollector.py 

This class is used to extract weather data from the external Web API, OpenWeatherMap API. 

- Used web requests to retrieve weather data from API. 
- Used "requests" module to make HTTP requests. 

"""

class WeatherDataCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
 
    #Method is responsible for getting weather data for particular city from OpenWeatherMap API. 
    def get_weather_data(self, city):

        #Using f-string to embed variables into string. 
        url = f"{self.base_url}?q={city}&appid={self.api_key}&units=metric"

        #Error Handling
        try:
            #Sending HTTP GET request to URL --> stores response from API into "response".
            response = requests.get(url)
            if response.status_code == 200: #Setting to 200 to indicate success. 
                data = response.json() #Extracts JSON data and assigns it to "data".
                return data

            else:
                print('Failed to retrieve weather data.')
                return None

        #If error (exception), run this block and print error. 
        except Exception as e:
            print("An error has occurred:", str(e))
            return None

#Method is responsible for printing weather data in legible format. 
def print_weather_data(weather_data):
    if weather_data is None: 
        print("Failed to get weather data. Ivalid city name or weather data not available.")
    else: 
        #Using error handling to catch an errors that may arise.
        try:  
            print("--------------> WEATHER DATA COLLECTOR CLASS RESULTS: ")

            print("Weather Information for", weather_data['name']) 
            print("Weather:", weather_data['weather'][0]['description'])
            print("Temperature:", weather_data['main']['temp'], "°C")
            print("Feels Like:", weather_data['main']['feels_like'], "°C")
            print("Minimum Temperature:", weather_data['main']['temp_min'], "°C")
            print("Maximum Temperature:", weather_data['main']['temp_max'], "°C")
            print("Pressure:", weather_data['main']['pressure'], "hPa")
            print("Humidity:", weather_data['main']['humidity'], "%")
            print("Wind Speed:", weather_data['wind']['speed'], "m/s")
            print("Sunrise Time:", weather_data['sys']['sunrise'])
            print("Sunset Time:", weather_data['sys']['sunset']) 
        
        except KeyError: #KeyError means that there is an issue with the key(s) in the dictionary data structure. 
            print("Ivalid city name or weather data not available.")

#Methods tests if API key valid key or not. 
def testing_api_key(api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}&units=metric'
    #Using error handling to catch an errors that may arise.
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('key is valid')
        else:
            print(f'API key is invalid. Status code: {response.status_code}') #Status code helps determine what type of error it is. 

    except Exception as e:
        print("An error has occurred:", str(e))

api_key = '37dfd4a9fb16f671fbc8618ed078efed'
#testing_api_key(api_key)

weather_collector = WeatherDataCollector(api_key) #Creating instance of WeatherDataCollector
city = input("Enter the name of the city: ") #Prompts user to type a city. 
weather_data = weather_collector.get_weather_data(city)
print_weather_data(weather_data)
