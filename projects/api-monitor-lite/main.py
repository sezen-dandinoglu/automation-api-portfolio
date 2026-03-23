###API Monitor Lite - checks multiple endpoints and prints status, response time, and a response preview.###

import requests
import time

URLS=["https://api.github.com", 
      "https://api.agify.io/?name=sezen", 
      "https://wrong-api-url.com"]

def check_api(url: str) -> None:
    print(f"\nChecking: {url}")
    start_time = time.perf_counter()

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        response_time = time.perf_counter() - start_time

        print(f"Status: {response.status_code} {response.reason} \n")
        print(f"Response time: {response_time:.2f} seconds")

        try:
            data = response.json()
            print("\nResponse Preview:\n")
            for key in list(data)[:3]:
                print(f"- {key}: {data.get(key)} \n")

        except ValueError:
            print("Response is not valid JSON")
            
    except requests.exceptions.ConnectionError:
        print(f"Conection error")

    except requests.exceptions.Timeout:
        print(f"Request timed out")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}") 

    print("-" * 50)    

def main() -> None:
    for url in URLS:
        check_api(url)

if __name__ == "__main__":
    main()