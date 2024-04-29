
import json
import requests

"""

DataTransformer.py 

This class is used to transform the raw weather data obtained from the external Web API, OpenWeatherMap API, to a more structured format and saving & loading data to & from JSON files. 

- Used file I/O to save and load transformed data to and from JSON files.
- Used "json" module for data serialization and deserialization. 

"""

class DataTransformer:
    #Method takes in raw_data and turns it into structured format. 
    #Required fields - 'Main', 'Weather', 'Wind' need to be present in raw data to extract more specfic info like temperature & humidity. 
    #Returns dictionary. 
    def transform_weather_data(self, raw_data): 
        transformed_data_dict = {}

        if 'main' in raw_data and 'weather' in raw_data and 'wind' in raw_data:
            main_data = raw_data['main']
            weather_data = raw_data['weather'][0]
            wind_data = raw_data['wind']

            transformed_data_dict.update({
                'temperature': main_data.get('temp'),
                'feels_like': main_data.get('feels_like'),
                'humidity': main_data.get('humidity'),
                'pressure': main_data.get('pressure'),
                'weather_description': weather_data.get('description'),
                'wind_speed': wind_data.get('speed'),
                'wind_deg': wind_data.get('deg')
            })
            
        
            return transformed_data_dict


    @staticmethod #Make static method bc doesn't need to access to instance variables. 
    def save_to_json(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod #Make static method bc doesn't need to access to instance variables. 
    def load_from_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data

# Example usage
transformer = DataTransformer()

city_name = input("Enter name of a city: ") #User prompt

base_url = "https://api.openweathermap.org/data/2.5/weather" #Stores the URL of the OpenWeatherMap API website. 
api_key = '37dfd4a9fb16f671fbc8618ed078efed' #Key that I created to access the API. 

#Parameters for API Request. 
params = {
    "q": city_name,
    "appid": api_key,
    "units": "metric"  
}

response = requests.get(base_url, params=params)
weather_data = response.json()


if response.status_code == 200:

    transformed_data_dict = transformer.transform_weather_data(weather_data)

    # Save transformed data to JSON
    transformer.save_to_json(transformed_data_dict, 'transformed_data_dict.json')

    # Load data from JSON
    loaded_data = transformer.load_from_json('transformed_data_dict.json')
    
    print("-----------------> DATA TRANSFORMER CLASS RESULTS: ")
    for key, value in loaded_data.items():
        print(key + ":", value)

else: 
    print("Error getting data.")