import datetime
import webbrowser
import DateTime
import speech_recognition as Srec
from pip import main
import pyttsx3
import wikipedia
import pyaudio
import subprocess
import os
from os import system, name

api = pyttsx3.init('sapi5')
voices = api.getProperty('voices')

api.setProperty('voice', voices[1].id)

valorant_path = "C:\\Riot Games\\VALORANT\\live\\VALORANT.exe"
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
        speak("Good Morning.")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon.")
    elif hour >= 17 and hour < 21:
        speak("Good Evening.")
    else:
        speak("Sweet Night.")
    speak("I'm ULTRA. Please tell me how may I help you?")


def speakAndprint(arg):
    speak(arg)
    print("\n", arg, "\n")


def listenYourMaster():

    sr = Srec.Recognizer()
    with Srec.Microphone() as source:
        print("Listening.....")
        sr.energy_threshold = 400
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


def defineYourSelf():
    speakAndprint(
        "Hello, I'm ULTRA. I'm a Desktop Assistant. I was created by my Master Jatin! I'm here to help you anytime!")


def openGoogle():
    speakAndprint("Opening It.....")
    url = "https://www.google.com"
    webbrowser.open(url)


def ask():
    speakAndprint("Okay. Please tell me how may I help you!")


def main():
    while True:
        query = listenYourMaster().lower()
        if 'hello' in query:
            speakAndprint("Hello!")

        elif 'who are you' in query:
            defineYourSelf()

        elif 'what are you' in query:
            defineYourSelf()

        elif 'why are you' in query:
            defineYourSelf()

        elif 'how are you' in query:
            speakAndprint("I'm Fine! How are you?")

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

        elif 'i am fine' in query:
            ask()

        elif 'i am not fine' in query:
            ask()

        elif 'open notepad' in query:
            speakAndprint("Opening Notepad.....")
            os.system("notepad.exe")

        elif 'open calculator' in query:
            speakAndprint("Opening Calculator.....")
            os.system("calc.exe")

        elif 'open wordpad' in query:
            speakAndprint("Opening Wordpad.....")
            os.system("calc.exe")

        elif 'open youtube' in query:
            speakAndprint("Opening Youtube.....")
            url = "https://www.youtube.com"
            webbrowser.open(url)

        elif 'search' in query:
            speakAndprint("Searching It.....")
            accept = query.replace("search", "")
            url = "https://www.google.com/search?q=" + accept
            webbrowser.open(url)

        # elif 'open game' in query:
        #     speakAndprint("Opening Valorant.....")
        #     subprocess.Popen(['C:\\Riot Games\\VALORANT\\live\\VALORANT.exe'])

        elif 'open google chrome' in query:
            openGoogle()

        elif 'open google' in query:
            openGoogle()

        elif 'open chrome' in query:
            openGoogle()

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            speakAndprint(result)

        elif 'thank you' in query:
            speakAndprint("Your Most Welcome.")

        elif 'quit' in query:
            speakAndprint("Thank you so much! Come back Soon!")
            exit()


if __name__ == "__main__":
    clear()
    wishYourMaster()
    main()
