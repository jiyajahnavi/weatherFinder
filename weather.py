import requests
import json

city = input("Please enter your city name\n")

url = f"https://api.weatherapi.com/v1/current.json?key=e2d51a4c20e14f9e99a80529243007&q={city}"

r = requests.get(url)

try: 
    print(f"Do you want all details about {city}")
    command = input("Please enter yes or no\n")
    if(command == "yes"):
        print(r.text)
except:
    print("Invalid input")
    
w = json.loads(r.text)
weather = w["current"]["temp_c"]

print(f"\n\nThe current weather in {city} is {weather} degrees")
print("Thank you")

