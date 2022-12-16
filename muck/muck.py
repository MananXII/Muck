
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
#import subprocess
#import ecapture as ec
#import wolframalpha
#import json
#import requests

print ('Loading MuCk')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
listener = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait





def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
         speak("Good Morning!")
    elif hour>=12 and hour<18:
         speak("Good Afternoon")
    else :
        speak("Good Evening!")




def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice =listener.lister(source)
            command= listener.recognize_google(voice)
            command= command.lower()

    try: 
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n") 

        except Exception as e:
            speak("i didn't hear you, please say that again")
            return "none"
        return statement 

speak("Loading muck")
wishMe()    


if __name__=='__main__':

    while True:
        speak("What can i do for you?")
        statement= takeCommand().lower()
        if statement==0:
            continue

        if "goodbye"in statement or "bye-bye"in statement or"turn off" in statement or "Bye muck" in statement or "Ok, bye muck"in statement:
            speak('see you later!')
            


            break

        if 'wikipedia' in statement: 
            speak('Searching the wiki') 
            statement =statement.replace("wikipedia", "") 
            results = wikipedia.summary(statement, sentences=3)
            speak("according to the wiki")
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://youtube.com")
            speak("youtube is now open")
            time.sleep(3)
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("gmail is now open")
            time.sleep(5)
        
        