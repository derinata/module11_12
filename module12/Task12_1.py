import requests
import sys

def fetch_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json() 
        return data.get("value")
    except requests.RequestException as e:
        print(f"Failed to fetch joke: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    
    joke = fetch_joke()
    if joke:
        print(joke)
    else:
        sys.exit(1)