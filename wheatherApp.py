import requests
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

city = input("enter a name of city for weather brodcast: ")
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

request = requests.get(url)
dict = json.loads(request.text)
speak.Speak(
    f"The Temperature of {city} is {int(dict['current']['temp_c'])} degree celcius"
)
print(f"The Temperature of {city} is : {int(dict['current']['temp_c'])} degree celcius")
