import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import random
import wikipedia #pip install wikipedia
import webbrowser
import re
import os
import sys
import requests
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am FRIDAY Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 500
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print(e) 
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'friday open youtube' in query:
            speak('Opening youtube')
            webbrowser.open("youtube.com")

        elif 'open youtube' in query:
            speak('Opening youtube')
            webbrowser.open("youtube.com")

        elif 'friday open google' in query:
            speak('Opening google')
            webbrowser.open("google.com")

        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open("google.com")

        elif 'friday open stackoverflow' in query:
            speak('Opening stackover flow')
            webbrowser.open("stackoverflow.com")  

        elif 'open stackoverflow' in query:
            speak('Opening stackover flow')
            webbrowser.open("stackoverflow.com")  

        elif 'friday are you there' in query:    
            speak(f"At your service sir") 

        elif 'are you there' in query:    
            speak(f"At your service sir") 

        elif 'friday are you listening' in query:    
            speak(f"At your service sir")

        elif 'are you listening' in query:    
            speak(f"At your service sir")

        elif 'friday can you listen me' in query:    
            speak(f"Very clearly sir")

        elif 'can you listen me' in query:    
            speak(f"very clearly sir")
        
        elif 'you listen me' in query:    
            speak(f"very clearly sir")


        elif 'friday play music' in query:
            music_dir = 'D:\\kapish\\music'
            songs = os.listdir(music_dir)
            print(songs) 
            speak('Playing Songs')   
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play music' in query:
            music_dir = 'D:\\kapish\\music'
            songs = os.listdir(music_dir)
            print(songs) 
            speak('Playing Songs')   
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'friday what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'friday open code' in query:
            speak('Opening Visual studio code')
            codePath = "C:\\Users\\kapis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open code' in query:
            speak('Opening Visual studio code')
            codePath = "C:\\Users\\kapis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'friday open notepad' in query:
            speak('Opening Notepad plus plus')
            codePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            speak('Opening Notepad plus plus')
            codePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(codePath)

        elif 'friday open dev' in query:
            speak('Opening Dev C plus plus')
            codePath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)

        elif 'open dev' in query:
            speak('Opening Dev C plus plus')
            codePath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)

        elif 'friday open chrome' in query:
            speak('Opening Google Chrome')
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            speak('Opening Google Chrome')
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'ok thank you' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'thank you friday' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()