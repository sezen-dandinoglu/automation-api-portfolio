import requests

URL="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=precipitation"

def main() -> None:
    will_rain = False

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        try:
            data = response.json()
            for i, hour in enumerate(data["hourly"]["precipitation"][:12]):
                if hour > 0:
                    will_rain = True
                    break
            
            if will_rain:
                time = data["hourly"]["time"][i]
                print("It will rain 🌧️\n")
                print(f"Time: {time} | Precipitation: {hour}")
            else: 
                print("No rain expected")

        except ValueError:
            print("Response is not valid JSON")
            
    except requests.exceptions.ConnectionError:
        print(f"Connection error")

    except requests.exceptions.Timeout:
        print(f"Request timed out")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}") 

if __name__ == "__main__":
    main()