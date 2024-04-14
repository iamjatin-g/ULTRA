import datetime
from AppOpener import open
from AppOpener import close
import webbrowser
import DateTime
import speech_recognition as Srec
from pip import main # type: ignore
import pyttsx3
# import pyaudio
import subprocess
import os
from os import system, name

api = pyttsx3.init('sapi5')
voices = api.getProperty('voices')

api.setProperty('voice', voices[1].id)

current = datetime.datetime.now()


def clear():
    if name == 'nt':
        screen = system('cls')
    else:
        screen = system('clear')


def speak(something):
    api.say(something)
    api.runAndWait()


def wishYourMaster():
    hour = int(datetime.datetime.now().hour)
    if hour >= 3 and hour < 12:
        speakAndprint("Good Morning.")
    elif hour >= 12 and hour < 17:
        speakAndprint("Good Afternoon.")
    elif hour >= 17 and hour < 21:
        speakAndprint("Good Evening.")
    else:
        speakAndprint("Sweet Night.")
    speakAndprint("I'm ULTRA. Please tell me how may I help you?")


def speakAndprint(arg):
    speak(arg)
    print("\n", arg, "\n")


def listenYourMaster():

    sr = Srec.Recognizer()
    with Srec.Microphone() as source:
        print("Listening.....")
        sr.energy_threshold = 100
        sr.pause_threshold = 1
        audio = sr.listen(source)

    try:
        print("Recognizing.....")
        query = sr.recognize_google(audio, language='en-in')
        print("User Said: ", query)

    except Exception as e:
        print("Can you Please say that again!")
        return "None"
    return query

def openGoogle():
    speakAndprint("Opening It.....")
    url = "https://www.google.com"
    webbrowser.open(url)

def defineYourSelf():
    speakAndprint(
        "Hello, I'm ULTRA. I'm a Desktop Assistant. I was created by my Master Jatin! I'm here to help you anytime!")

def ask():
    speakAndprint("Okay. Please tell me how may I help you!")

def main():
    while True:
        query = listenYourMaster().lower()
        if 'hello' in query or 'hi' in query or 'hey' in query:
            speakAndprint("Hello!")
            ask()

        elif 'who are you' in query or 'what are you' in query or 'why are you' in query or 'how are you' in query:
            defineYourSelf()

        elif 'good morning' in query or 'good afternoon' in query or 'good evening' in query or 'good night' in query:
            wishYourMaster()

        elif 'date' in query:
            date_now = current.strftime("%d %b, %Y ")
            sp_date = "It's " + str(date_now)
            speakAndprint(sp_date)

        elif 'time' in query:
            time_now = current.strftime(
                " %I hours %M minutes %S seconds of %p ")
            sp_time = "It's " + str(time_now)
            speakAndprint(sp_time)

        elif 'day' in query:
            day_now = current.strftime("%A")
            sp_day = "It's " + str(day_now)
            speakAndprint(sp_day)

        elif 'month' in query:
            month_now = current.strftime("%B")
            sp_month = "It's " + str(month_now)
            speakAndprint(sp_month)

        elif 'year' in query:
            year_now = current.year
            sp_year = "It's " + str(year_now)
            speakAndprint(sp_year)

        elif 'i am fine' in query or 'i am not fine' in query:
            ask()

        elif 'notepad' in query:
            speakAndprint("Opening Notepad.....")
            os.system("notepad.exe")

        elif 'calculator' in query:
            speakAndprint("Opening Calculator.....")
            os.system("calc.exe")

        elif 'wordpad' in query:
            speakAndprint("Opening Wordpad.....")
            os.system("write.exe")

        elif 'google' in query:
            open("chrome")

        elif 'list applications' in query:
            open("LS")

        elif 'da vinci resolve' in query:
            speakAndprint("Opening Da Vinci Resolve.....")
            open("davinci resolve")

        elif 'youtube' in query:
            speakAndprint("Opening Youtube.....")
            url = "https://www.youtube.com"
            webbrowser.open(url)

        elif 'whatsapp' in query:
            speakAndprint("Opening Whatsapp.....")
            url = "https://web.whatsapp.com/"
            webbrowser.open(url)

        elif 'netflix' in query:
            speakAndprint("Opening Netflix.....")
            url = "https://www.netflix.com/"
            webbrowser.open(url)

        elif 'hotstar' in query:
            speakAndprint("Opening Hotstar.....")
            url = "https://www.hotstar.com/"
            webbrowser.open(url)

        elif 'github' in query:
            speakAndprint("Opening Github.....")
            url = "https://github.com/"
            webbrowser.open(url)

        elif 'telegram' in query:
            speakAndprint("Opening Telegram.....")
            url = "https://web.telegram.org/"
            webbrowser.open(url)

        elif 'open google chrome' in query:
            openGoogle()

        elif 'open google' in query:
            openGoogle()

        elif 'open chrome' in query:
            openGoogle()

        elif 'open' in query:
            speakAndprint("Please Wait, I'll try to Open It.....")    
            accept = query.replace("open", "")
            open(accept)

        elif 'close' in query:
            speakAndprint("Please Wait, I'll try to Close It.....")
            accept = query.replace("close", "")
            close(accept)

        elif 'search' in query:
            speakAndprint("Searching It.....")
            accept = query.replace("search", "")
            url = "https://www.google.com/search?q=" + accept
            webbrowser.open(url)

        elif 'thank you' in query:
            speakAndprint("Your Most Welcome.")

        elif 'exit' in query or 'quit' in query or 'bye' in query or 'bye bye' in query:
            speakAndprint("Take care! Come back Soon!")
            exit()

if __name__ == "__main__":
    clear()
    wishYourMaster()
    main()
