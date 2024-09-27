import time

def setWallpaper():
    
    current_time = time.localtime()
    current_hour = current_time.tm_hour

    print(f"Current Hour:{current_hour}")
    if current_hour<12 and current_hour>6:
        return "Weather App/Resources/sunrise.jpg"
    
    elif current_hour >=12 and current_hour<17 :
        return "Weather App/Resources/sun.jpg"
    elif current_hour>=17 and current_hour<19:
        return "Weather App/Resources/sunset.jpg"
    elif current_hour>=19 or current_hour<6:
        return "Weather App/Resources/night.jpg"
    






