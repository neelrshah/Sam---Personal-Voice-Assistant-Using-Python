 
import speech_recognition as sr
import pyttsx3
import datetime
from win32 import win32gui
from win32.lib import win32con
import pyjokes
import pyautogui
import wolframalpha
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    except Exception as err:
        speak('please connect microphone')

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("I couldn't get you sir ")
        return "None"
    return query



def wishMe():
    # this function wishes user according to time
    hour = int(datetime.datetime.now().hour)
    speak("Welcome back sir")
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 
# wishMe()



def login():
    # this is login function
    speak('starting all system applications and installing all drivers')
    # Minimize = win32gui.GetForegroundWindow()
    # win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE) 
    speak('Establishing Secured Connections')
    speak('now i am online sir')
    speak('Please tell me how may I help you')
# login()



def goOffline():
    # this function is user to turn off assistant.
    speak('ok sir')
    speak('closing all systems')
    speak('disconnecting to servers')
    quit()



# this function is used to get time.
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    print(Time)
    speak("current time is:")
    speak(Time)
# time()



# this function is used to get date.
def date():
    Year = int(datetime.datetime.now().year)
    Month =int(datetime.datetime.now().month)
    Date = int(datetime.datetime.now().day)
    speak("Today's date is ")
    speak(Date)
    speak(Month)
    speak(Year)
# date()



# function to answer how are you.
def whoAreYou():
    speak('I am Sam !, Your personal Assistant')



# function to answer who made you.
def whoMadeYou():
    speak('I was Created by xyz')



# this function is used to get jokes.
def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)



# This function is used to take screenshot
def takeScreenshot():
    img = pyautogui.screenshot()
    img.save("ss.png")
    print("ScreenShot Taken")
# takeScreenshot()



def mathsCalculation(input):
    # write your wolframalpha app_id here 
    try:
        app_id = "PWKTU6-JHJ24GYJL6" 
        client = wolframalpha.Client(app_id) 
        indx = input.lower().split().index('calculate') 
        query = input.split()[indx + 1:] 
        res = client.query(' '.join(query)) 
        answer = next(res.results).text 
        speak("The answer is " + answer) 
        print(answer)
    except:
        speak("Sorry Sir, Something went wrong,Please try again")

    return


