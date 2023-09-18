from jarvisUi import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QMovie

import pyttsx3 as st
import speech_recognition as sr
from PyQt5.QtCore import QThread, QTimer
import sys

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.task_gui()

    def Speak(self, text):
        Assistant = st.init("sapi5")
        voices = Assistant.getProperty('voices')
        Assistant.setProperty('voices', voices[0].id)
        Assistant.setProperty('volume', 1000)
        Assistant.setProperty('rate', 170)

        print(f"Your text: {text}\n")

        Assistant.say(text)
        Assistant.runAndWait()

    def takeCommand(self):
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            command.pause_threshold = 1
            audio = command.listen(source, 0, 7)

            try:
                print("Recognizing....")
                query = command.recognize_google(audio, language='en')
                print(f"You said: {query.lower()}")
            except Exception as Error:
                return None
            query = str(query).lower()
        return query

    def task_gui(self):
        self.query = self.takeCommand()
        if 'hello' in self.query:
            self.Speak("hello sir")

startFunction = MainThread()

class Gui_Start(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)

        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):
        self.jarvis_ui.movies = QMovie("used/Nt6v.gif")
        self.jarvis_ui.label_2.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()

        self.jarvis_ui.movies = QMovie("used/loader.gif")
        self.jarvis_ui.label_3.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()

        self.jarvis_ui.movies = QMovie("used/initiater.gif")
        self.jarvis_ui.label_4.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()

        self.jarvis_ui.movies = QMovie("used/Health_Template.gif")
        self.jarvis_ui.label_5.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()

        self.jarvis_ui.movies = QMovie("used/hacker bg.gif")
        self.jarvis_ui.label_6.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()

        startFunction.start()
        
    def runTaskExecution(self):
        # This method will be called after a 1-second delay
        # It ensures that the main window is open before starting taskExecution
        self.jarvis_ui.label.setText("Main Window is ready!")

        # Now you can start your taskExecution
        taskExecution()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Gui_Start()
    window.show()
    sys.exit(app.exec_())
