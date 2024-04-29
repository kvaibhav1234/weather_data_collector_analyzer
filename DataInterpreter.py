
from DataAnalyzer import DataRetriever

class DataInterpreter:


    """

    DataInterpreter.py 

    This class is used to load the transformed the data into a format that is easily interpreted, read, and understood to a human. 

    """
    #Initialization Method 
    def __init__(self, data_retriever):
        self.data_retriever = data_retriever #Allows DataInterpreter object to access methods from DataRetriever object. 

    #Method displayers weather data summary in legible format. 
    def display_weather_summary(self, city_name):
        weather_data = self.data_retriever.get_weather_data(city_name)

        if weather_data:
            print("-------------> DATA INTERPRETER CLASS RESULTS: Weather Summary:")

            city = weather_data.get('name', 'Unknown City')
            temperature = weather_data.get('main', {}).get('temp', 'N/A')
            feels_like = weather_data.get('main', {}).get('feels_like', 'N/A')
            humidity = weather_data.get('main', {}).get('humidity', 'N/A')
            pressure = weather_data.get('main', {}).get('pressure', 'N/A')
            weather_description = weather_data.get('weather', [{}])[0].get('description', 'N/A')
            wind_speed = weather_data.get('wind', {}).get('speed', 'N/A')
            wind_deg = weather_data.get('wind', {}).get('deg', 'N/A')

            print(f"City: {city}")
            print(f"Temperature: {temperature} °C")
            print(f"Feels Like: {feels_like} °C")
            print(f"Humidity: {humidity}%")
            print(f"Pressure: {pressure} hPa")
            print(f"Weather Description: {weather_description}")
            print(f"Wind Speed: {wind_speed} m/s")
            print(f"Wind Degree: {wind_deg}°")
            print("-" * 30)
        else:
            print("Failed to retrieve weather data.")

#Code that should run only when this script is executed directly.
if __name__ == "__main__":
    api_key = '37dfd4a9fb16f671fbc8618ed078efed' 
    retriever = DataRetriever(api_key)
    interpreter = DataInterpreter(retriever)
    city_name = input("Enter name of a city: ")
    interpreter.display_weather_summary(city_name)