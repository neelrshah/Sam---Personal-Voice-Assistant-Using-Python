
import requests, json
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # It takes microphone input from the user and returns string output
    rw = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            rw.pause_threshold = 1
            audio = rw.listen(source)
    except Exception as err:
        speak('please connect microphone')

    try:
        print("Recognizing...")    
        query = rw.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# base URL
def getWeather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    speak("Which Cities weather should i search for?")
    CITY = takeCommand()
    API_KEY = "6ca7340a21f9f7a7206759667ab7057b"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        print(f"{CITY:-^30}")
        speak("Current temperature is:" + str(temperature))
        speak("Humidity is:" + str(humidity))
        speak("Pressure is:" + str(pressure))
        speak("Weather is:" + str(report[0]['description']))
        
        # print(f"Temperature: {temperature}")
        # print(f"Humidity: {humidity}")
        # print(f"Pressure: {pressure}")
        # print(f"Weather Report: {report[0]['description']}")
    else:
        # showing the error message
        print("Error in the HTTP request")
        speak("Can't find weather at this time")

# getWeather()