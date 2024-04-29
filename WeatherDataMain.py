

from WeatherDataCollector import WeatherDataCollector
from DataTransformer import DataTransformer
from DataAnalyzer import DataAnalyzer, DataRetriever
from DataInterpreter import DataInterpreter

import matplotlib.pyplot as plt

"""

WeatherDataMain.py 

- Used to conduct the weather data collecting, transforming, analyzing, and visualizing processes. 

"""

class WeatherDataMain:
    
    def __init__(self, api_key): #Need api_key for collecting the data.  
        self.api_key = api_key 
        #Creating instances of the relevant classes needed to run this project. 
        self.data_collector = WeatherDataCollector(api_key) 
        self.data_transformer = DataTransformer() 
        self.analyzer = None
        self.interpreter = None
        self.data_retriever = DataRetriever(api_key)

    #Method is responsible for retrieving data for specific city, transforming the data, and analying the data to find avg. temp., max. wind speed, and # of rainy days. 
    def run(self):
        city = input("Enter the name of the city: ")

        #Using exception handling to catch potential errors that may arise. 
        try: 
            weather_data = self.data_collector.get_weather_data(city)
            if weather_data:
                    transformed_data = self.data_transformer.transform_weather_data(weather_data) #Transforms weather data using transform_weather_data from DataTransformer class. 
                    transformed_data['city'] = city
                    self.analyzer = DataAnalyzer(transformed_data) #Analyzes data based on functions from DataAnalyzer class. 
                    self.interpreter = DataInterpreter(self.data_retriever)
                    self.interpreter.display_weather_summary(city)  # Display weather summary before analysis
                    self.analyze_and_visualize_data(transformed_data)
            else:
                print(f"Failed to retrieve weather data for the city '{city}'. Please check the city name and try again.")
        except Exception as e: 
            print(f"An error occurred while retrieving weather data for the city '{city}': {str(e)}")

    #Method analyzes transformed data. 
    def analyze_and_visualize_data(self, transformed_data):
        if not transformed_data:
            print("No weather data available.")
            return

        #Utilizing functions from DataAnalyzer class and storing values in variables. 
        average_temp = self.analyzer.average_temperature()
        max_wind = self.analyzer.max_wind_speed()
        humidity = self.analyzer.humidity()

        print("-----------------------> DATA ANALYZER CLASS RESULTS:")
        average_temp = self.analyzer.average_temperature()
        print("Average temperature:", average_temp, "°C")
        max_wind = self.analyzer.max_wind_speed()
        print("Max wind speed:", max_wind, "m/s")
        humidity = self.analyzer.humidity()
        print("Humidity:", humidity, "%")


        weather_data = self.interpreter.data_retriever.get_weather_data(transformed_data['city']) #Retrieves data for specific city which uses the DataRetriever object in the DataInterpreter instance. 

        if weather_data:
            city = weather_data.get('name', 'Unknown City')
            temperature = weather_data.get('main', {}).get('temp', 'N/A')
            feels_like = weather_data.get('main', {}).get('feels_like', 'N/A')
            humidity = weather_data.get('main', {}).get('humidity', 'N/A')
            pressure = weather_data.get('main', {}).get('pressure', 'N/A')
            weather_description = weather_data.get('weather', [{}])[0].get('description', 'N/A')
            wind_speed = weather_data.get('wind', {}).get('speed', 'N/A')
            wind_deg = weather_data.get('wind', {}).get('deg', 'N/A')

        #Output for Weather Data Analysis for current class. 
        print("---------------> WEATHER DATA MAIN CLASS RESULTS: ")
        print("Average temperature:", average_temp, "°C")
        print("Max wind speed:", max_wind, "m/s")
        print("Number of rainy days:", humidity)

        self.visualize_data([transformed_data])

    #Data Visualization!  
    def visualize_data(self, data): 
        if not data:
            print("No weather data available.")
            return

        plt.figure(figsize=(2.5, 5))
        for entry in data:
            city = entry['city']
            temperature = entry['temperature']
            plt.bar(city, temperature, color='pink')

        plt.title('Average Temperature')
        plt.xlabel('City')
        plt.ylabel('Temperature (°C)')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--')
        plt.tight_layout()
        plt.show()

#Implementation Usage
api_key = '37dfd4a9fb16f671fbc8618ed078efed'
weather_main = WeatherDataMain(api_key)
weather_main.run()
