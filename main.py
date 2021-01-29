from features import *
import random
import os
import win32gui, win32con
import psutil
import subprocess
import webbrowser
import pyttsx3 as p
import wikipedia
from selenium import webdriver
import wolframalpha
from news import speak_news
from weather import getWeather
from PyDictionary import PyDictionary




paths = {'documentPath' : "C:\\Users\\neelr\\Documents", 'downloadPath' : "C:\\Users\\neelr\\Downloads" ,
         'musicPath' : "C:\\Users\\neelr\\Music",'picturesPath' : "C:\\Users\\neelr\\Pictures" ,
         'videosPath' : "C:\\Users\\neelr\\Videos",'chrome_path' : 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
         'executable_path' : "C:\chromedriver_win32\chromedriver"}

class recom():
    def __init__(self):
        self.driver = self.driver = webdriver.Chrome(paths['executable_path'])
    def recom_info(self):
        try:
            self.driver.get(url="https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")
            select = self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]')
            select.click()
        except Exception as e:
            print(e)



class YoutubeAutomation():
    def __init__(self):
        self.driver = webdriver.Chrome(paths['executable_path'])
    def play(self, name):
        self.name = name
        self.driver.get(url="https://www.youtube.com/results?search_query="+ name)
        video = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        video.click()



if __name__ == "__main__":
    wishMe()

    dictionary = PyDictionary()
    try:
        search_list = [x.lower() for x in dictionary.synonym("search")]
        open_list = [x.lower() for x in dictionary.synonym("open")]
        song_list = [x.lower() for x in dictionary.synonym("song")]
        restart_list = [x.lower() for x in dictionary.synonym("restart")]
        shutdown_list = [x.lower() for x in dictionary.synonym("shutdown")]
    except(Exception):
        print("An exception occurred")

    login()
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(paths['chrome_path']))

    while True:
        query = takeCommand().lower()
        
        try:
            searchRes = any(ele in query for ele in search_list)
            openRes = any(ele in query for ele in open_list)
            songRes = any(ele in query for ele in song_list)
            restartRes = any(ele in query for ele in restart_list)
            shutdownRes = any(ele in query for ele in shutdown_list)
        except:
            print("An exception occurred")


        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        
        elif query in ['hi','hey','whatsup','whatsapp','sup','hello'] :
            d = random.choice(['hey','hi','hello'])
            speak(d)

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'who are you' in query:
            whoAreYou()

        elif 'who made you' in query:
            whoMadeYou()

        elif (('open' in query or 'show' in query or openRes) and 'documents' in query):
            speak("sure sir")
            os.startfile(paths["documentPath"]) 

        elif (('open' in query or 'show' in query or openRes) and 'downloads' in query):
            speak("sure sir")
            os.startfile(paths["downloadPath"]) 

        elif (('open' in query or 'show' in query or openRes) and 'pictures' in query):
            speak("sure sir")
            os.startfile(paths["picturesPath"]) 

        elif (('open' in query or 'show' in query or openRes) and 'videos' in query):
            speak("sure sir")
            os.startfile(paths["videosPath"])

        elif ('joke' in query or 'jokes' in query ):
            jokes()

        elif 'open google' in query:
            speak("sure sir")
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stackoverflow' in query:
            speak("sure sir")
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

        elif 'search' in query or searchRes:
            try:
                speak('What do you want to search for?')
                search = takeCommand()
                url = 'https://google.com/search?q=' + search
                webbrowser.get('chrome').open_new_tab(url)
                speak('Here is What I found for' + search)
            except:
                speak("Sorry Sir, I could not find it")

        elif ('remember that' in query ):
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif ("information" in query or 'wikipedia' in query):
            speak('Searching in Wikipedia...')
            if 'wikipedia' in query:
                query = query.replace("wikipedia", "")
            if 'information' in query:
                query = query.replace("information", "")
            try:
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e1:
                print(e1)
                speak("Sorry Sir!,I couldnt find it on wikipedia ,Please say it again!")

        elif ("recommendation" in query or 'recomend' in query):
            engine.say("Here are a list of movies you can choose to watch from")
            engine.runAndWait()
            bot = recom()
            bot.recom_info()

        elif(songRes):
            r5 = sr.Recognizer()
            engine.say("what should i play?")
            engine.runAndWait()
            with sr.Microphone() as source3:
                audio4 = r5.listen(source3)
                try:
                    video = r5.recognize_google(audio4)
                    bot = YoutubeAutomation()
                    bot.play(video)
                except sr.UnknownValueError:
                    print("")
                    speak("Something went wrong, Try Again")
                except sr.RequestError as e:
                    print("")
                    speak("Something went wrong, Try Again")

        # youtube automation
        elif ("music" in query or 'song' in query or "video" in query or 'youtube' in query ):
            r5 = sr.Recognizer()
            engine.say("what should i play?")
            engine.runAndWait()
            with sr.Microphone() as source3:
                audio4 = r5.listen(source3)
                try:
                    video = r5.recognize_google(audio4)
                    bot = YoutubeAutomation()
                    bot.play(video)
                except sr.UnknownValueError:
                    print("")
                    speak("Something went wrong, Try Again")
                except sr.RequestError as e:
                    print("")
                    speak("Something went wrong, Try Again")

        elif 'logout' in query or shutdownRes and ['pc' in query or 'laptop' in query or 'desktop' in query]:
            speak("sure sir")
            os.system("shutdown -l")

        elif 'screenshot' in query:
            takeScreenshot()
            speak('screenshot taken')


        elif ('shutdown' in query or shutdownRes and ['pc' in query or 'laptop' in query or 'desktop' in query]):
            speak("sure sir")
            os.system("shutdown /s /t 1")

        elif ('restart' in query or restartRes and ['pc' in query or 'laptop' in query or 'desktop' in query]):
            speak("sure sir")
            os.system("shutdown /r /t 1")

        
        elif ('cpu' in query and ('usage' in query or 'percent' in query)):
            usage=str(psutil.cpu_percent())
            speak("CPU usage is" +usage)

        elif ('battery' in query and ('usage' in query or 'percent' in query)):
            battery = psutil.sensors_battery()
            speak("Battery is at an ")
            speak(battery.percent)

        elif ('ram' in query and ('usage' in query or 'percent' in query)):
            ram =psutil.virtual_memory()
            speak("RAM used is "+ str(psutil.virtual_memory()[2]))

        elif "calculate" in query or 'convert' in query or 'solve' in query: 
            mathsCalculation(query)  

        elif 'news' in query:
            speak('Ofcourse sir..')
            speak_news()
    

        elif 'weather' in query:
            getWeather()

        elif 'go offline' in query:
            goOffline()

