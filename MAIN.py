
import subprocess

def install_module(module_name):
    try:
        __import__(module_name)
    except ImportError:
        print(f"{module_name} is not installed. Installing...")
        try:
            subprocess.check_call(["pip", "install", module_name], shell=True)
            print(f"{module_name} has been successfully installed.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {module_name}. Error: {str(e)}")
            
# List of required modules
required_modules = [
    "random",
    "jarvis",
    "googletrans",
    "pywhatkit",
    "pyttsx3",
    "pyautogui",
    "watsapp",
    "keyboard",
    "wikipedia",
    "geopy",
    "playsound",
    "requests",
    "PyDictionary",
    "bs4",
    "PyPDF2",
    "gtts",
    "winsound",
    "speedtest",
    "pywikihow",
    "wolframalpha"
]

for module in required_modules:
    install_module(module)

import wolframalpha
from jarvis import Speak,takeCommand,takeHindi
import webbrowser
from googletrans import  Translator
import pywhatkit
import os
import pyttsx3 as st
import time
import pyautogui
from watsapp import Message
import keyboard
import wikipedia
import os
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import keyboard
from playsound import playsound
import requests
import datetime
from PyDictionary import PyDictionary as dic
import requests
from bs4 import BeautifulSoup
import PyPDF2
from gtts import gTTS
import winsound
import random
import speedtest
from pywikihow import search_wikihow


command_1 = [
    "hello",
    "hey",
    "hi",
    "assistant",
    "okay",
    "alright",
]

replies1 = [
    "hello, sir. welcome back!",
    "good day, sir. how can i assist you?",
    "greetings, sir. how may i be of service?",
    "hello there, how can i assist you today?",
    "i'm at your service, sir. how can i help?",
    "good to see you again, sir. what's on your mind?",
    "welcome back, sir. what can i do for you?",
    "hello, sir. how can i assist you today?",
    "greetings, sir. it's a pleasure to assist you.",
    "hello again, sir. what can i do for you?",
    "sir, i'm ready to assist. what do you need?",
    "at your service, sir. how may i assist you?",
    "hello, there! how can i make your day better?",
    "it's a pleasure to see you again, sir. what's your command?",
    "welcome back, sir. how can i be of help?",
    "good day, sir. how can i brighten your day?",
    "greetings, sir. i'm here to assist you in any way i can.",
    "hello, sir. what's on your agenda today?",
    "i'm here, sir. what can i do for you?",
    "at your service, sir. how can i assist you today?",
    "hope you're having a great day, sir. how can i help?",
]

goodbye_commands = ["bye",
    "goodbye",
    "see you later",
    "take care",
    "until next time",
    "bye for now",
    "see you soon",
    "goodnight",
    
    "later",
    "bye-bye",
    "go and sleep",
    "nighty-night",
    "see you tomorrow",
]

bye_responses = [
    "goodbye, sir. feel free to return whenever you need assistance.",
    "bye for now, sir. i'll be here when you're ready.",
    "see you later, sir. have a great day!",
    "take care, sir. don't hesitate to reach out when you need help.",
    "until next time, sir. have a wonderful day!",
    "goodbye, sir. stay well and take care.",
    "farewell, sir. i'm just a command away when you need me.",
    "alright, sir. bye! feel free to come back anytime.",
    "bye-bye, sir. wishing you a fantastic day!",
    "later, sir. have a productive day!",
    "goodbye, my friend. don't be a stranger!",
    "bye, sir. remember, i'm here to assist you anytime.",
    "take it easy, sir. goodbye for now!",
    "until we meet again, sir. have a wonderful day ahead!",
    "adios, sir. have a splendid day!",
    "au revoir, sir. see you on the flip side!",
    "ciao, sir. don't forget you have a trusty assistant here!",
    "cheerio, sir. stay awesome!",
    "till next time, sir. have a fantastic day!",
    "sayonara, sir. your assistant is at your service!",
]




def WolfRam(query):     #not used yet
    api_key="P444L6-6V99WGHW34"
    requester = wolframalpha.Client(api_key)
    extracter = requester.query(query)

    try:
        Answer = next(requested.results).text
        return Answer
    except :
        Speak("An String Value is not Answerable.")

def Speaktotime():
    dic = {i: i - 12 for i in range(13, 25)}
    return

def Trans():
    Speak("Tell me the line!")
    Line = takeHindi()
    traslate = Translator()
    result= traslate.translate(Line)
    Text = result.text
    Speak("Translation is : " +Text)

def get_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        address = data.get('city')  # You can change 'city' to 'loc' or 'region', depending on the level of detail you want.
        return address
    except Exception as e:
        print(f"Error retrieving location information: {e}")
        return None
def chrome_auto(query):
    command =query.replace("chrome page command","")
    command= command.replace("jarvis","")

   

    if 'scroll' in command:
        # Scroll the page down by pressing the 'Down' arrow key
        keyboard.press_and_release('down')
    elif 'scroll up' in command:
        # Scroll the page up by pressing the 'Up' arrow key
        keyboard.press_and_release('up')
    elif 'new tab' in command:
        # Open a new tab by pressing Ctrl + T
        keyboard.press_and_release('ctrl + t')
    elif 'close tab' in command:
        # Close the current tab by pressing Ctrl + W
        keyboard.press_and_release('ctrl + w')
    elif 'switch tab' in command:
        # Switch to Tab 2 by pressing Ctrl + 2
        keyboard.press_and_release('ctrl + 2')

    
def WolfRam(query):
    query=query.replace("jarvis","")
    # Wolfram Alpha free API endpoint
    query = query.replace(" ","+")
    api_url = f"https://api.wolframalpha.com/v2/query?input={query}&format=image,plaintext&output=JSON&appid=DEMO"
    
    
    
    
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div", class_="BNeawe").text

    Speak(f"The {query} is : ")
    Speak(temperature)

def dict(query):
    query =query.replace("What is the ","")
    query= query.replace("jarvis","")
    if 'meaning' in query:        
        prob=query.replace("what is the meaning of","")
        
        result = dic.meaning(prob)
        Speak(f"meaning of {prob} is {result}")
    elif 'synonym' in query:        
        prob=query.replace("what is the synonym of","")
        
        result = dic.meaning(prob)
        Speak(f"synonym of {prob} is {result}")

    elif 'antonym' in query:        
        prob=query.replace("what is the antonym of","")
        
        result = dic.meaning(prob)
        Speak(f"antonym of {prob} is {result}")
    return

def YTAutomate(query):
    
    command =query.replace("youtube command","")
    command= command.replace("jarvis","")
        
        
        
  
    if 'pause' or 'pose' in command:
        keyboard.press('space')
    elif 'restart' in command:
        keyboard.press('0')
    elif 'skip' in command or 'next' in command:
        keyboard.press('l')  # 'l' key to skip to the next video
    elif 'back' in command or 'previous' in command:
        keyboard.press('j')  # 'j' key to go back to the previous video
    elif 'mute' in command:
        keyboard.press('m')
    elif 'volume up' in command:
        keyboard.press('up')
    elif 'volume down' in command:
        keyboard.press('down')
    
    elif 'fullscreen' in command:
        keyboard.press_and_release('f')
def rename():
 # Specify the new directory path
    directory = "C:/Users/Rajeev Khare/Pictures/Screenshots"


    # List all files and directories in the specified directory
    files_and_directories = os.listdir(directory)

    # Use a list comprehension to count only files (not directories)
    file_count = len([item for item in files_and_directories if os.path.isfile(os.path.join(directory, item))])
    
    new_directory = "C:/Users/Rajeev Khare/Pictures/Screenshots"

    # Change the current working directory to the new directory
    os.chdir(new_directory)
    
    old_path = "C:/Users/Rajeev Khare/Pictures/Screenshots/screenshot.png"
    new_path = f"C:/Users/Rajeev Khare/Pictures/Screenshots/screenshot{file_count+1}.png"
    os.rename(old_path,new_path)
    i+=1

def Temp(query):
    query=query.replace("jarvis","")
    query=query.replace("what is the","")
    url = "https://www.google.com/search?q="+query
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div", class_="BNeawe").text

    Speak(f"The {query} is : ")
    Speak(temperature)

def Speed():
    Speak("Checking Speed....")
    tester = speedtest.Speedtest()
    downloading = tester.download()
    correctDown = int(downloading/800000)
    uploading = tester.upload()
    correctup = int(uploading/800000) 

    Speak(f"the downloading speed is {correctDown} mbp s and uploading speed is {correctup} mbp s")


    
def openApp(query):
    
    Speak("Ok sir! wait a second")
    #i have a doubt have to change my own
    if 'vs code' in query:
        os.startfile("C:\Program Files\Microsoft VS Code\Code.exe")
    elif 'youtube' in query:
        Speak("Wait A second ")
        web = 'https://www.youtube.com'
        webbrowser.open(web)
        Speak("youtube is opened Sir")
    elif 'telegram' in query:
        Speak("Wait A second ")
        web = 'https://www.telegram.com'
        webbrowser.open(web)
        Speak("Telegram is opened Sir")
    elif 'instagram' in query:
        Speak("Wait A second ")
        web = 'https://www.instagram.com'
        webbrowser.open(web)
        Speak("instagram is opened Sir")
    elif 'facebook' in query:
        Speak("Wait A second ")
        web = 'https://www.facebook.com'
        webbrowser.open(web)
        Speak("facebook is opened Sir")
    elif 'eda playground' in query:
        Speak("Wait A second ")
        web = 'https://edaplayground.com/playgrounds/user/539694'
        webbrowser.open(web)
        Speak("eda playground is opened Sir")
    elif 'chatgpt' in query:
        Speak("Wait A second ")
        web = 'https://chat.openai.com/'
        webbrowser.open(web)
        Speak("Chatgpt is opened Sir")
    elif 'amazon' in query:
        Speak("Wait A second ")
        web = 'https://www.amazon.in/'
        webbrowser.open(web)
        Speak("amazon is opened Sir")
    elif 'chrome' in query:
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

    else :
        Speak("not a valid Website Sir")

def closeApp(query):
    Speak("Ok sir! wait a second")
    if any(keyword in query for keyword in ['youtube', 'instagram', 'facebook', 'eda playground', 'chatgpt', 'amazon', 'chrome']):
      os.system("TASKKILL /F /im chrome.exe")

    
def Reader(query):
    
    name = query.replace("read book", "")
    if 'hindi' in name:
        boolean = True
        name = name.replace("hindi", "")
    else:
        boolean =False
        name = name.replace("english", "")
    
    if 'final report' in name:
        pdf_path = r"C:\Users\Rajeev Khare\Downloads\FINAL-REPORT 1.pdf"
        os.startfile(pdf_path)

        with open(pdf_path, 'rb') as book:
            pdfReader = PyPDF2.PdfReader(book)
            num_pages = len(pdfReader.pages)
            Speak(f"Number of pages in this PDF are {num_pages}")
            Speak("From which page should I start reading?")
            num_page = int(input("Tell page number"))
            
            if 0 <= num_page < num_pages:
                page = pdfReader.pages[num_page]
                text = page.extract_text()
                
            else:
                Speak("Invalid page number. Please choose a valid page.")

        
        if boolean ==True:
            trans1=Translator()
            textHin=trans1.translate(text,'hi')
            textm = textHin.text
            speech = gTTS(text = textm)
            try:
                speech.save('book.mp3')
                playsound('book.mp3')
                
            except :
                playsound('book.mp3')
                
                
        if boolean==False :
            trans1=Translator()
            textHin=trans1.translate(text,'en')
            textm = textHin.text
            speech = gTTS(text = textm)
            try:
                speech.save('book.mp3')
                playsound('book.mp3')
                
            except :
                playsound('book.mp3')


def taskExecution(): # will take input from user infinte times
    while True :
        query = takeCommand()
        for word in query.split():
            if word in command_1:
                response = random.choice(replies1) + ","
                Speak(response)
            elif word in goodbye_commands:
                response = random.choice(bye_responses) + ","
                Speak(response)
                
        try :
            
          
           
            if 'youtube search' in query :
                # if 'latest' in query:
                Speak("Ok sir,this is what i found for your search")
                query=query.replace("jarvis","")
                query= query.replace("youtube search","")
                query=query.replace("latest","")
                web = 'https://www.youtube.com/results?search_query='+query
                webbrowser.open(web)

                Speak("Searching Done Sir")
                pywhatkit.playonyt(query)
                Speak("This is the latest video for your search")

                # else:

                #     Speak("Ok sir,this is what i found for your search")
                #     query=query.replace("jarvis","")
                #     query= query.replace("youtube search","")
                #     web = 'https://www.youtube.com/results?search_query='+query
                #     webbrowser.open(web)

                #     Speak("Searching Done Sir")
                

            

            elif 'google search' in query :
                Speak("Ok sir,this is what i found for your search Sir!")
                query=query.replace("jarvis","")
                query= query.replace("google search","")
                pywhatkit.search(query)
                import wikipedia as googlscrap
                
                query=query.replace("google","")
                

                try:
                   
                    note = googlscrap.summary(topic,2)
                    print("----------->>>" ,note)
                    Speak(note)
            
                except :
                    Speak("Sorry, NO speakable Data found")
            
            elif 'launch website' in query :
                query=query.replace("jarvis","")
                query= query.replace("launch website","")
                
                try:
                    web = 'https://www.' +query+ '.com'
                    webbrowser.open(web)
                    Speak("Launching done sir!")
                except :
                    Speak("Invalid website")

            elif 'wikipedia search' in query:
                try:
                    topic = query.replace("wikipedia search", "")
                    summary = wikipedia.summary(topic)
                    print("Summary:", summary)
                    Speak(summary)
            
                except :
                    Speak("Sorry, I could not understand your command.")

            
                

            elif 'one movies tv' in query:
                        query=query.replace("Search","")
                        # query=query.replace("in","")
                        query = query.replace("one movies tv","")
                        query = query.replace("1moviestv","")
                        query=query.replace("jarvis","")
                        query = query.replace(" ","-")
                        web=f'https://1moviestv.com/search/{query}'
                        webbrowser.open(web)
                        
            elif 'play a song' in query :
                
                query=query.replace("jarvis","")
                query=query.replace("play a song","")
                if query == "omg 2" :
                    os.startfile('C:\\Users\Rajeev Khare\\Downloads\\omg2.mp3')
                    Speak("Song has launched!, enjoy Sirr!")
                else:
                    pywhatkit.playonyt(query)

            elif 'whatsapp' in query:
               Message(query)

            elif 'what is the' in query:
                
                if 'temperature' in query:
                    WolfRam(query)
                elif 'speed' in query:
                    Speed()
                else:
                    dict(query)

            elif 'screenshot' in query:
                kk = pyautogui.screenshot()
                kk.save("C:\\Users\\Rajeev Khare\\Pictures\\Screenshots\\screenshot.png")  # Specify a filename with the .png extension
                rename()
                Speak("Screenshot taken and saved, Sir!")

                Speak("Screenshot taken and saved, Sir!")

            elif 'open' in query:
                query = query.replace("open ","")
                query=query.replace("jarvis","")
                openApp(query)

            elif 'close' in query:
                if 'command' not in query:
                    query = query.replace("close","")
                    query=query.replace("jarvis","")
                    closeApp(query)
                else:
                    pass

            elif 'youtube command' in query:
                YTAutomate(query)

            elif 'chrome page command' in query:
                chrome_auto(query)
                
            elif 'set alarm' in query:
                # dic= {i:i+12 for i in range(13,25)}
                dic1 ={i:f'0{i}' for i in range(1,10)}

                Speak("tell me the time !")
                time = takeCommand()

                # if 'evening' in time:
                #     time = time.replace(" evening ","")
                #     print(time)
                    
                #     poping = True
                # else:
                #     poping =False
                
                time = time.replace(" and ", " ")
                time = time.replace(".", " ")
                
                splitter = time.split(" ")
                print(splitter)
                splitter=[int(splitter[0]),int(splitter[1])]
                # if poping==True :
                #     splitter[0]=dic[splitter[0]]
                # else:
                #     pass
                if splitter[0] <10 :
                    
                    splitter[0]=int(dic1[splitter[0]])
                
                # if splitter[0] < 
                
                if splitter[1] < 10 :
                    splitter[1]=int(dic1[splitter[1]])
                else:
                    pass
                time = f'{splitter[0]}:{splitter[1]}:00'
                print(time)
                

                while True:
                    current_time_Extract = datetime.datetime.now()
                    
                    current_time = current_time_Extract.strftime("%H:%M:%S")
                    
                    if current_time == time:
                        Speak("Times up")
                        playsound(r'C:\Users\Rajeev Khare\Music\Iron Man - Bgm.mp3')

                        Speak("Alarm  closed!")
                    elif current_time>time:
                        break
            elif 'translate' in query:
                Trans()
            elif 'remind me' in query:
                rememMsg = query.replace("remind me","")
                rememMsg = rememMsg.replace("jarvis","")
                Speak("You tell me to remind you that : " +rememMsg)
                with open('data.txt','w') as file:
                    file.write(rememMsg)
            elif 'reminder message'  in query:
                rememMsg = query.replace("remind me","")
                rememMsg = rememMsg.replace("jarvis","")
                with open('data.txt','r') as file:
                    reminder =file.read()
                Speak("Your reminder message is :"+reminder)
            elif 'read book' in query:
                Reader(query)
            elif 'how to' in query:
                query = query.replace("how to","")
                Speak("Getting Data from Internet.....")
                max_result = 1
                how_to_func = search_wikihow(query,max_result)
                assert len(how_to_func)==1
                how_to_func[0].print()
                Speak(how_to_func[0].summary)
            else :
                pass

        
        except :
            
        
            Speak("Sorry Sir, i didn't Understood")
            Speak("can you repeat sir")
            
        if query in goodbye_commands:
            break
            
            
            
            
    


taskExecution()