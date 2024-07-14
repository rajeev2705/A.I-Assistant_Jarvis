import os
import speech_recognition as sr
import pyttsx3
import random
import webbrowser
import pywhatkit
import wikipedia as googlscrap
import pyautogui
from datetime import datetime
import re
import google.generativeai as genai
import requests
import json
import psutil
from gtts import gTTS
import pygame
from googletrans import Translator
from spotipy.oauth2 import SpotifyOAuth
import spotipy

translator = Translator()

API_KEY_OPENWEATHERMAP = 'your_openweathermap_api_key_here'
API_KEY_IPGEOLOCATION = 'your_ipgeolocation_api_key_here'
COUNT_FILE_PATH = r"D:\New folder\question_count.txt"
LOG_FILE_PATH = r"D:\New folder\interactions_log.txt"
SCREENSHOT_DIRECTORY = "D:/New folder/Screenshots"

username = 'YourUsernameHere'
clientID = 'your_client_id_here'
clientSecret = 'your_client_secret_here'
redirect_uri = 'http://google.com/callback/'

# Spotify API setup
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
print(json.dumps(user_name, sort_keys=True, indent=4))

# Google AI API setup
current_key_index = 0
question_count = 0

# Configuration and constants
SOFTWARES = ["notepad", "chrome", "kai cad"]
SOFTWARE_PATHS = [
    r"C:\Windows\notepad.exe",
    
    r"C:\Program Files\KiCad\8.0\bin\kicad.exe"
    #add more software paths
]

API_KEYS = [
    "xxxxxxxxxxxxxxxxxxxx" #can add more api keys if you have multiple accounts for ai response
    
]

GREETING_COMMANDS = [
    "hello", "hey", "assistant", "okay", "alright",
    "namaste", "kaise", "theek", "sab thik",
    "kya hal hai", "kya chal raha hai", "kaise ho", "kaise hain"
]

GREETING_RESPONSES = [
    "hello, sir. welcome back",
    "good day, sir. how can i assist you",
    "greetings, sir. how may i be of service",
    "hello there, how can i assist you today",
    "i'm at your service, sir. how can i help",
    "good to see you again, sir. what's on your mind",
    "welcome back, sir. what can i do for you",
    "hello, sir. how can i assist you today",
    "greetings, sir. it's a pleasure to assist you",
    "hello again, sir. what can i do for you",
    "sir, i'm ready to assist. what do you need",
    "at your service, sir. how may i assist you",
    "hello, there! how can i make your day better",
    "it's a pleasure to see you again, sir. what's your command",
    "welcome back, sir. how can i be of help",
    "good day, sir. how can i brighten your day",
    "greetings, sir. i'm here to assist you in any way i can",
    "hello, sir. what's on your agenda today",
    "i'm here, sir. what can i do for you",
    "at your service, sir. how can i assist you today",
    "hope you're having a great day, sir. how can i help"
]

GOODBYE_COMMANDS = ["bye", "goodbye", "see you later", "alvida", "fir milenge", "phir milenge", 'aram kar le', "so ja"]

GOODBYE_RESPONSES = [
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
    "sayonara, sir. your assistant is at your service!"
]

common_hindi_words = [
    "hoon", "hai", "the", "thi", "tha", "kya", "kaise", "kahan", "kab", "kyon",
    "kaun", "namaste", "dhanyavad", "kripya", "maaf", "haan", "nahin",
    "thak", "jaldi", "dheere",
    "andar", "bahar", "yahan", "wahan", "sab", "kuch"
]

def detect_language(text):
    words = text.split()
    for word in words:
        if word.lower() in common_hindi_words:
            print("hindi")
            return 'hindi'
    print("english")
    return 'english'

def convert_to_hindi(text):
    translated = translator.translate(text, src='en', dest='hi')
    print(translated.text)
    return translated.text

def play_song(song_name):
		search_song = song_name
		results = spotifyObject.search(search_song, 1, 0, "track") 
		songs_dict = results['tracks'] 
		song_items = songs_dict['items'] 
		song = song_items[0]['external_urls']['spotify'] 
		webbrowser.open(song) 
		


genai.configure(api_key=API_KEYS[current_key_index])
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config)
chat_session = model.start_chat(history=[])


def switch_api_key():
    global current_key_index
    current_key_index = (current_key_index + 1) % len(API_KEYS)
    genai.configure(api_key=API_KEYS[current_key_index])



def get_current_location():
    try:
        url = f'https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY_IPGEOLOCATION}'
        response = requests.get(url)
        location_data = response.json()
        
        if 'city' in location_data:
            city = location_data.get('city', 'Unknown City')
            region = location_data.get('region', 'Unknown Region')
            country = location_data.get('country_name', 'Unknown Country')
            return f"You are currently in {city}, {region}, {country}."
        else:
            return "Unable to determine current location."
    except Exception as e:
        return f"Error: {str(e)}"


def get_weather(city, api_key):
    try:
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(base_url)
        weather_data = response.json()
        
        if weather_data['cod'] == 200:
            main = weather_data['main']
            weather = weather_data['weather'][0]
            temperature = main['temp']
            feels_like = main['feels_like']
            description = weather['description']
            return f"Current weather in {city}: {description}. Temperature: {temperature}°C. Feels like: {feels_like}°C."
        else:
            return "Unable to fetch weather information."
    except Exception as e:
        return f"Error: {str(e)}"
    
def get_ai_response(question):
    global question_count
    question_count += 1
    if question_count > 50:
        switch_api_key()
        question_count = 1

    response = chat_session.send_message(question)
    return response.text


def search_website(query):
    match = re.search(r'(\w+)\s+search\s+(.*)', query)
    if match:
        website, search_query = match.groups()
        search_query = search_query.strip()
        if website == 'youtube':
            url = f'https://www.youtube.com/results?search_query={search_query}'
        elif website == 'google':
            url = f'https://www.google.com/search?q={search_query}'
        elif website == '1moviestv':
            url = f'https://www.1moviestv.com/search?q={search_query}'
        else:
            url = f'https://{website}.com/search?q={search_query}'

        speak(f"Searching {website} for {search_query}")
        webbrowser.open(url)
        speak("Search completed.")
    else:
        speak("Sorry, I didn't understand the command.")


# def speak(text):
#     response = text
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id)
#     engine.setProperty('rate', 150)
#     engine.setProperty('volume', 10)
#     print(f"Your text: {response}\n")
#     engine.say(response)
#     engine.runAndWait()


def speak_hindi(sentence):
    # Convert text to speech in Hindi
    tts = gTTS(text=sentence, lang='hi')
    audio_file = 'hindi_speech.mp3'
    tts.save(audio_file)

    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load and play the audio file
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        continue

def speak(response_text):
    global language
    if language == 'hindi':
        # Convert response to Hindi
        response_text = convert_to_hindi(response_text)
        # Speak in Hindi
        speak_hindi(response_text)
    else:
        # Speak in English
        response_text=response_text.replace("*","")
        response_text=response_text.replace("?","")

        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 10)
        print(f"Your text: {response_text}\n")
        engine.say(response_text)
        engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source, 0, 7)

        try:
            print("Recognizing....")
            query = recognizer.recognize_google(audio, language='en')
            print(f"You said: {query.lower()}")
        except Exception as Error:
            return None
        return str(query).lower()


def update_question_count():
    global question_count

    if os.path.exists(COUNT_FILE_PATH):
        with open(COUNT_FILE_PATH, "r") as count_file:
            try:
                question_count = int(count_file.read().strip())
            except ValueError:
                question_count = 0
    else:
        question_count = 0

    question_count += 1

    with open(COUNT_FILE_PATH, "w") as count_file:
        count_file.write(str(question_count))


def log_interaction(query):
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(f"Question: {query}\n")
        ai_response = get_ai_response("give short summary in 3 or 5 lines covering all aspects " + query)
        ai_response_clean = re.sub(r'[*#]', '', ai_response)
        log_file.write(f"AI Response: {ai_response_clean}\n\n")


def execute_task():
    query = take_command()
    global language
    language = detect_language(query)
    if query is None:
        pass

    update_question_count()
    log_interaction(query)

    if any(cmd in query for cmd in GREETING_COMMANDS):
        response = random.choice(GREETING_RESPONSES) + ","
        speak(response)
    elif any(cmd in query for cmd in GOODBYE_COMMANDS):
        response = random.choice(GOODBYE_RESPONSES) + ","
        speak(response)
        return 
    elif 'youtube search' in query:
        handle_youtube_search(query)
    elif 'google search' in query:
        handle_google_search(query)
    elif 'wikipedia search' in query:
        handle_wikipedia_search(query)
    elif 'screenshot' in query:
        take_screenshot()
    elif 'open' in query:
        open_software(query)
    elif 'tell me' in query:
        ai_response = get_ai_response(query)
        speak(ai_response)
    elif 'current location' in query:
        response = get_current_location()
        speak(response)
    elif 'weather' in query:
        if 'today' in query:
            location_str = "You are currently in Chandigarh, Unknown Region, India."
            pattern = r"You are currently in (\w+),.*?, (\w+)\."
            matches = re.search(pattern, location_str)
            if matches:
                city = matches.group(1)
                country = matches.group(2)
            # Assume today's weather for current location
                response = get_weather(city, API_KEY_OPENWEATHERMAP)
                speak(response)
        else:
            # Ask for the city or location for weather information
            ai_response ="Which city or country's weather would you like to know?"
            speak(ai_response)
            city_country = take_command()
            response = get_weather(city_country, API_KEY_OPENWEATHERMAP)
            speak(response)
    elif 'play song' or ' play ' or 'gaana chalao' in query:
        speak("What song would you like to play?")
        song_name = take_command()
        if song_name:
            speak('Song is going to play') 
            play_song(song_name)

        else:
            speak("Sorry, I didn't catch that. Please say the song name again.")
    
    elif 'close' or 'band karo' in query:
        query = query.replace("close", "").replace("jarvis", "").strip()
        closeApp(query)

    else:
        pass


def closeApp(process_name):
    processes = scan_running_user_processes()
    if not processes:
        print("No user processes found.")
        return
    if any(process_name.lower() in process['name'].lower() for process in processes):
        kill_process_by_name(process_name)
    else:
        print("terminated/n")

def handle_youtube_search(query):
    try:
        speak("This is what I found on YouTube")
        pywhatkit.playonyt(query)
        speak("Done, sir")
    except Exception as e:
        speak("An unknown error occurred. Please try again.")
        print(e)


def handle_google_search(query):
    try:
        speak("This is what I found on Google")
        pywhatkit.search(query)
        speak("Done, sir")
    except Exception as e:
        speak("An unknown error occurred. Please try again.")
        print(e)


def handle_wikipedia_search(query):
    try:
        speak("Searching Wikipedia...")
        query = query.replace("Wikipedia", "")
        result = googlscrap.summary(query, sentences=2)
        
        speak("According to Wikipedia, " + result)
    except Exception as e:
        speak("An unknown error occurred. Please try again.")
        print(e)


def take_screenshot():
    try:
        speak("Taking screenshot...")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(SCREENSHOT_DIRECTORY, f"{timestamp}.png")
        pyautogui.screenshot(screenshot_path)
        speak("Screenshot taken successfully.")
        rename_screenshot(screenshot_path)
    except Exception as e:
        speak("An error occurred while taking the screenshot. Please try again.")
        print(e)


def rename_screenshot(screenshot_path):
    new_directory = SCREENSHOT_DIRECTORY
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    filename = os.path.basename(screenshot_path)
    new_path = os.path.join(new_directory, filename)
    os.rename(screenshot_path, new_path)
    print(f"Screenshot renamed and moved to {new_path}")


def open_software(query):
    for software, path in zip(SOFTWARES, SOFTWARE_PATHS):
        if software in query:
            try:
                os.startfile(path)
                speak(f"{software.capitalize()} is now opening.")
            except Exception as e:
                speak(f"Failed to open {software}. Please check the path and try again.")
                print(e)
            return
    speak("Software not recognized. Please try again.")

def is_user_process(process):
    try:
        # Filter out system processes based on various criteria
        if process.username() in ['SYSTEM', 'NT AUTHORITY\\SYSTEM', 'root']:  # Example usernames for system processes
            return False
        
        if 'windows' in process.exe().lower():  # Example: Exclude processes containing 'windows' in executable path
            return False
        
        # Add more conditions as needed based on process attributes or other criteria
        return True
    
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False

def scan_running_user_processes():
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if is_user_process(process):
                process_info = process.as_dict(attrs=['pid', 'name', 'username'])
                processes.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes

def kill_process_by_name(process_name):
    killed = False
    for process in psutil.process_iter(['pid', 'name']):
        try:
            process_info = process.as_dict(attrs=['pid', 'name'])
            if process_name.lower() in process_info['name'].lower() and is_user_process(process):
                process.terminate()
                # print(f"Process '{process_info['name']}' (PID: {process_info['pid']}) terminated successfully.")
                killed = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    if not killed:
        print(f"No user process matching '{process_name}' found or could not terminate.")

def main():
    while True:
        print("Listening for commands...")
        execute_task()

def wakeup():
    while True:
        try:
            wake_up = take_command()

            if wake_up and 'wake up' in wake_up:
                main()
              
            else:
                pass  # Break out of the wake-up loop and return to main execution
           
        except Exception as e:
          
                pass        

# if __name__ == "__main__":
wakeup()
