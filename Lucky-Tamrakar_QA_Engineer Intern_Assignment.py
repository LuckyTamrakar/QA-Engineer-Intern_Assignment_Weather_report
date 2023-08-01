import requests


def get_weather_data():
    base_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get weather data.")
        return None

def get_weather(weather_data, date):
    for item in weather_data["list"]:
        if item["dt_txt"] == date:
            return item["main"]["temp"]
    return None

def get_wind_speed(weather_data, date):
    for item in weather_data["list"]:
        if item["dt_txt"] == date:
            return item["wind"]["speed"]
    return None

def get_pressure(weather_data, date):
    for item in weather_data["list"]:
        if item["dt_txt"] == date:
            return item["main"]["pressure"]
    return None



weather_data = get_weather_data()
if not weather_data:
    exit()

while True:
    print("\nOptions:")
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    option = int(input("Select an option: "))

    if option == 1:
        date = input("Enter the date (format: 'YYYY-MM-DD HH:MM:SS'): ")
        temperature = get_weather(weather_data, date)
        if temperature is not None:
            print(f"Temperature on {date}: {int(temperature)-273}°C")
        else:
            print("Data not available for the specified date.")

    elif option == 2:
        date = input("Enter the date (format: 'YYYY-MM-DD HH:MM:SS'): ")
        wind_speed = get_wind_speed(weather_data, date)
        if wind_speed is not None:
            print(f"Wind speed on {date}: {wind_speed} m/s")
        else:
            print("Data not available for the specified date.")

    elif option == 3:
        date = input("Enter the date (format: 'YYYY-MM-DD HH:MM:SS'): ")
        pressure = get_pressure(weather_data, date)
        if pressure is not None:
            print(f"Pressure on {date}: {pressure} hPa")
        else:
            print("Data not available for the specified date.")

    elif option == 0:
        break

    else:
        print("Invalid option. Please select a valid option.")