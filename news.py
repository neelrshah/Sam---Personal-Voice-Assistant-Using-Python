import requests
import json
import pyttsx3
from features import takeCommand
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speak_news():
    # API KEY : de6ab7c3e50143308b3461c9e2a31333
    global_url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=de6ab7c3e50143308b3461c9e2a31333'

    local_url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=de6ab7c3e50143308b3461c9e2a31333'

    speak("Which new would you like to Hear? Global or Local")
    newsType = takeCommand().lower()

    if('global' in newsType):
        url = global_url
    elif('local' in newsType):
        url = local_url

    try:    
        news = requests.get(url).text
        news_dict = json.loads(news)
        arts = news_dict['articles']
        speak('Todays Headlines are..')
        for index, articles in enumerate(arts):
            speak(articles['title'])
            if index == len(arts)-1:
                break
            speak('Moving on the next news headline..')
        speak('These were the top headlines, Have a nice day Sir!!..')
    except:
        speak("Sorry Sir, Some Error occured in fetching news. Please try again")


if __name__ == '__main__':
    speak_news()