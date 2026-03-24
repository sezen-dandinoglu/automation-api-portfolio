###API Monitor Lite - checks multiple endpoints and prints status, response time, and a response preview.###

import requests
import time
from datetime import datetime
import os

URLS=["https://api.github.com", 
      "https://api.agify.io/?name=sezen", 
      "https://wrong-api-url.com"]


def check_api(url: str) -> int | None:
    print(f"\nChecking: {url}")
    start_time = time.perf_counter()
    status_code=None

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        response_time = time.perf_counter() - start_time
        status_code=response.status_code

        print(f"Status: {status_code} {response.reason} \n")
        print(f"Response time: {response_time:.2f} seconds")

        try:
            data = response.json()
            print("\nResponse Preview:\n")
            for key in list(data)[:3]:
                print(f"- {key}: {data.get(key)} \n")

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

    return status_code

def main() -> None:
    succeed_request_count=0
    failed_request_count=0

    for url in URLS:
        status_code=check_api(url)
        
        if status_code and 200 <= status_code < 300: 
            succeed_request_count +=1
        else: 
            failed_request_count +=1

    try:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "api_log.txt")

        lines = [
            f"Run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
            f"Success: {succeed_request_count}", 
            f"Failed: {failed_request_count}",
            "-" * 50
            ]
        
        with open(file_path, "a", encoding = 'utf-8') as file:
            for line in lines:
                file.write(f"{line}\n")

    except PermissionError:
        print("Error: You do not have permission to read 'api_log.txt'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()