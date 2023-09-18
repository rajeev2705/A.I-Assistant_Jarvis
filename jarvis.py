import pyttsx3 as st
import speech_recognition as sr
from googletrans import Translator


def Speak(text): #jarvis output generator
    Assistant = st.init("sapi5")
    voices = Assistant.getProperty('voices')
    Assistant.setProperty('voices',voices[0].id)
    Assistant.setProperty('volume',1000)
    Assistant.setProperty('rate',170)
   
    
    print(f"Your text : {text}")
    print(" ")

    Assistant.say(text)
    Assistant.runAndWait()

def takeCommand():   # taking input from user
    command = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....")
        command.pause_threshold  =1
        audio = command.listen(source,0,7)

        try :
            print("Recognizing....")
            query = command.recognize_google(audio,language = 'en')
            print(f"You said : {query.lower()}")
        except Exception as Error:
            return None
        query = str(query).lower()
    return query

def takeHindi():   # taking input from user
    command = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....")
        command.pause_threshold  =1
        audio = command.listen(source,0,7)

        try :
            print("Recognizing....")
            query = command.recognize_google(audio,language = 'hi')
            print(f"You said : {query}")
        except Exception as Error:
            return None
        query = query.lower()
    return query


    


        