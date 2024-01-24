import requests

def get_weather(api_key, location):
    # OpenWeatherMap API endpoint for current weather
    api_url = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API request
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can use 'imperial' for Fahrenheit
    }

    # Make the API request
    response = requests.get(api_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract relevant weather information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        # Display weather information
        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print(f"Error: Unable to fetch weather data. Status code {response.status_code}")

def main():
    # Prompt the user to enter the name of a city or a zip code
    location = input("Enter the name of a city or a zip code: ")

    # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
    api_key = "5bfce1fce784bfaa0145ef6729fd37a6"

    # Get and display weather information
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
