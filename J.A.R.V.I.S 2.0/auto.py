import os
import speech_recognition as sr
import pyttsx3


def talk(text):
    jarvis = pyttsx3.init('sapi5')
    voices = jarvis.getProperty('voices')
    jarvis.setProperty('voice', voices[0].id)
    jarvis.setProperty('rate', 190)
    jarvis.setProperty('volume', 1.0)
    jarvis.say(text)
    jarvis.runAndWait()


def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        listener.pause_threshold = 1
        voice = listener.listen(source)
        try:
            command =''
            command = listener.recognize_google(voice)
            print("Recognizing...")
            command = command.lower()

        except:
            pass
        return command


while True:

    wake_up = take_command()
    print(wake_up)
    if 'wake up' in wake_up:
        os.startfile('F:\pythonProject1\J.A.R.V.I.S_2.0.py')
        talk('waking up')
    else:
        print('did not recognize')
        take_command()
