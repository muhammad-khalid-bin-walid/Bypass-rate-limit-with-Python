import requests
import time
import random

def get_user_input():
    url = input("Please enter the URL: ")
    return url

def exponential_backoff(url, retries=5, initial_delay=1):
    delay = initial_delay
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
            delay *= 2
            if delay > 60:  # Maximum delay
                delay = 60
    return None

# Get the URL from the user
url = get_user_input()

# Perform the exponential backoff
response = exponential_backoff(url)
if response:
    print("Success:", response.content)
else:
    print("Failed to retrieve data after several attempts.")
