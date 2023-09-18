import os
import speech_recognition as sr

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

while True:
    try:
        wake_up =takeCommand()

        if 'wake up' in wake_up :
            os.startfile("D:\my jarvisis\Jarvis\MAIN.py")
        
        else :
            pass
    except :
        wake_up =takeCommand()

        if 'wake up' in wake_up :
            os.startfile("D:\my jarvisis\Jarvis\MAIN.py")
        
        else :
            pass