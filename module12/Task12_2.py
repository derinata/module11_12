import os
import sys
import requests

def fetch_weather(city: str, api_key: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    description = data["weather"][0]["description"]
    celsius = data["main"]["temp"]  # already in Celsius with units=metric
    return description, celsius

if __name__ == "__main__":
    api_key = ("1ba6d3faff35e1a0ffbf96052f0e1405")
    if not api_key:
        print("ERROR: OPENWEATHER_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(2)

    city = input("Enter municipality name: ").strip()
    if not city:
        sys.exit(1)

    try:
        description, temp_c = fetch_weather(city, api_key)
    except requests.HTTPError as e:
        # API returned an error (e.g., city not found); show brief message on stderr
        print(f"Failed to fetch weather: {e}", file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Network error: {e}", file=sys.stderr)
        sys.exit(1)

    # Print only the required output: description and temperature in Celsius
    print(f"{description}, {temp_c:.1f}°C")