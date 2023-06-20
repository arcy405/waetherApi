import requests
import json
import os

city = input("Enter the city\n")

url = "https://api.weatherapi.com/v1/current.json?key=820df8902d064736874101813232006&q={city}"

r = requests.get(url)
print(r.text)

# print(type(r.text))

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

os.system(f"say 'The current temparature in {city} is {w} degrees'")