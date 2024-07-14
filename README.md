AI Assistant Program
Overview
This program is a voice-controlled AI assistant capable of performing various tasks through voice commands. It leverages different APIs and libraries to execute actions like opening applications, performing web searches, playing music, retrieving weather information, and more.

Features
Voice Control: Activate the assistant by saying "wake up".
Command Capabilities: Execute tasks such as:
Opening software applications (open notepad).
Performing web searches on Google (google search how to use Python).
Playing songs on Spotify (play song Shape of You).
Getting weather information (weather in New York).
Taking screenshots (take screenshot).
Interacting with Wikipedia (wikipedia search Artificial Intelligence).
Language Support: Supports commands in both Hindi and English; automatically detects the language for responses.
Setup Instructions
API Configuration:

Obtain API keys for services like OpenWeatherMap, IPGeolocation, and generative AI.
Replace placeholders in the code (API_KEY_OPENWEATHERMAP, API_KEY_IPGEOLOCATION, API_KEYS) with your actual API keys.
Software Configuration:

Customize SOFTWARES and SOFTWARE_PATHS lists to match the applications you want to open with voice commands.
Dependencies:

Install required Python packages using pip install -r requirements.txt.
Ensure all dependencies are installed and up-to-date.
Usage
Starting the Assistant:

Run Main.py to start the assistant.
Interacting with the Assistant:

Say "wake up" to activate the assistant.
Speak commands naturally (e.g., "play song", "weather in city", "open software").
Voice Commands:

Speak clearly and wait for the assistant to process your command.
Use Hindi or English interchangeably; the assistant detects and responds accordingly.
Additional Notes
Adjust settings and functionalities in the code to suit your specific needs.
Ensure a stable internet connection for web-based functionalities.