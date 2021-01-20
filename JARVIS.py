import datetime as datetime
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\Lansman Computer\\OneDrive\\Pictures\\Camera Roll.png")

def time_():
    Time = datetime.datetime.now().strftime("%H: %M: %S")
    speak("the current time is")
    speak(Time)

def Date_():
    Year = datetime.datetime.now().year
    Month = datetime.datetime.now().month
    Day = datetime.datetime.now().day
    speak("The current date is")
    speak(Day)
    speak(Month)
    speak(Year)

def wishMe():
    speak("Glad to have you back Demola")
    time_()
    Date_()

    #greetings

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Goodmorning Charles")

    elif hour>= 12 and hour <18:
        speak("Goodafternoon Demola")
    elif hour >= 18 and hour<= 24:
        speak("Goodevening Demola")

    else:
        speak("Goodnight Demola")

    speak("Charlie at your service , please how can i help you today ?")

def TakeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.........")
        r.pause_threshold = 1 #this tells how long it will take for the user to talk
        audio = r.listen(source)

    try:
        print('Recognizing......')
        query = r.recognize_google(audio, language='en-US') #this variable will store whatever we say
        print(query)

    except Exception as e:
        print(e)
        print("say that again please...")
        return 'None'

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)  #587 is the port for gmail
    server.ehlo()   #this will help in identifying us to an smtp server
    server.starttls()   #this will help us in putting the smtp server into tls

    server.login('username@gmail.com', 'password')
    server.sendmail('username@gmail.com', to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU percent is '+ usage)

    battery = psutil.sensors_battery()
    speak('Battery is at...')
    speak(battery)

def jokes():
    speak(pyjokes.get_jokes())


if __name__ == "__main__":

    wishMe()

    while True:
        query = TakeCommand().lower()

        #all commands will be stored in lower case for easy recognition

        if 'time' in query: #if time is in the question asked
            time_()
        if 'date' in query: #if date is in the question asked
            Date_()

        elif 'wikipedia' in query:
            speak('searching....')
            query = query.replace('wikipedia','') #this ensure we dont store unneccessary words
            result = wikipedia.summary(query, sentences=4)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak('what should i say ?')
                content = TakeCommand()
                #provide receiver email
                speak("who is the receiver")
                receiver = input("enter receiver's email :")
                to = receiver
                sendEmail(to, content)
                speak(content)
                speak('Email has been sent')

            except Exception as e:
                print(e)
                speak('Unable to send email')

        elif 'search in chrome ' in query:
            speak('what do you want me to search ?')
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'search youtube' in query :
            speak('what should i search ?')
            search_input = TakeCommand().lower()
            speak('here we go to youtube !')
            wb.open('https://www.youtube.com/results?search_query=' + search_input)

        elif 'search google' in query:
            speak('what should i search ?')
            search_term = TakeCommand().lower()
            speak('searching...')
            wb.open('https://www.google.com/search?q=' + search_term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'go offline' in query:
            speak('going offline sir')
            quit()

        elif 'word' in query:
            speak('opening ms word...')
            ms_word = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013'
            os.startfile(ms_word)

        elif 'take note' in query:
            speak('what should i write sir')
            notes = TakeCommand().lower()
            file = open('notes.txt', 'w')
            speak('sir should i include date and time ?')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done taking notes sir')

            else:
                file.write(notes)

        elif 'show me' in query:
            speak('showing notes sir')
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()

        elif 'play music' in query:
            songs_dir = 'C:\\Users\Lansman Computer\Music\iTunes'
            music = os.listdir(songs_dir)
            speak('what should i play sir ?')
            speak('select a number..')
            ans = TakeCommand().lower()
            while('number' not in ans and ans != 'random' and ans != 'you choose'):
                speak('i could not understand you. please try again')
                ans= TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number', ''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(1, 100)
            os.startfile(os.path.join(songs_dir, music[no]))

        elif 'remind me' in query:
            speak('what should i remind you sir ?')
            memory = TakeCommand()
            speak('you asked me to remind you that '+ memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            speak('yes i do sir')
            remember=open('memory.txt', 'r')
            speak('you asked me to remind you that' + remember.read())














