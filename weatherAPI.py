import requests
import json
import pyttsx3


def weather(city):
    data=requests.get(f"https://api.weatherapi.com/v1/current.json?key=/*YOUR API KEY*/&q={city}")
    formatedData=data.json()
    tempData=f"{formatedData["current"]["temp_c"]}°C"
    windData=f"{formatedData["current"]["wind_mph"]} ᵐᵖʰ"
    uvData=f"{formatedData["current"]["uv"]}"
    humidityData=f"{formatedData["current"]["humidity"]}"
    print(tempData)
    print(humidityData)
    print(windData)
    print(uvData)

    return tempData,humidityData,windData,uvData
   


