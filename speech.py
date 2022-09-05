from vosk import Model, KaldiRecognizer
import pyttsx3
import datetime
import pyaudio
import os
import msvcrt as m
import pyjokes
import wikipedia
import random
import pygame
from time import sleep
import requests
import webbrowser as wb
from bs4 import BeautifulSoup
import wikipedia as googleScrap


def wait():
    m.getch()


APRIL = pyttsx3.init('sapi5')
voice = APRIL.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_EvaM'
rate = APRIL.getProperty('rate')
APRIL.setProperty('rate', 170)
voices = APRIL.getProperty('voices')
APRIL.setProperty('voice', assistant_voice_id)



def speak(audio):
    print('APRIL: ' + audio)
    APRIL.say(audio)
    APRIL.runAndWait()


k1=["loading data, this may take some time","loading models, this usualy take some time"]
rand=random.choice(k1)
speak(rand)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 3 and hour < 12:
        remember = open("Remember.txt", "r")
        speak('Good morning ' + remember.read()+'. it is a great day today')
        Time = datetime.datetime.now().strftime('%I %M %p')
        speak('the time is')
        speak(Time)


    elif hour >= 12 and hour < 18:
        remember = open("Remember.txt", "r")
        speak('Good afternoon '+ remember.read())
        Time = datetime.datetime.now().strftime('%I %M %p')
        speak('the time is')
        speak(Time)

    elif hour >= 18 and hour < 20:
        remember = open("Remember.txt", "r")
        speak('Good evening ' + remember.read())
        Time = datetime.datetime.now().strftime('%I %M %p')
        speak('the time is')
        speak(Time)
    elif hour >= 20 and hour < 22:
        Time = datetime.datetime.now().strftime('%I %M %p')
        speak('the time is')
        speak(Time)
        speak('how can i help you sir ')


    elif hour >= 22 and hour < 3:
        remember = open("Remember.txt", "r")
        speak('it is late' + remember.read())
        speak('it is')
        Time = datetime.datetime.now().strftime('%I %M: %p')
        speak(Time)
        speak('How can I help you now')
        print('')
        print('listening ...')
        print('')

model = Model(r"C:\Users\asmid\PycharmProjects\vosk\vosk-model-en-in-0.5\vosk-model-en-in-0.5")
recognizer = KaldiRecognizer(model, 16000)
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
a = 0




def command():

    print("")
    print("Listening...")
    print("")

    while True:

        data = stream.read(4000, exception_on_overflow=False)

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            p = text[14:-3]
            print(f"You Said : {p}")
            if len(p) > 0:
                return p

            else:
                print('Sorry, I did\'t get that. :( Try typing the command, (tips: type 10 instead of "ten") ')
                query = str(input('your favor is: '))
                return query


for i in range(3):
    speak("PLEASE SPEAK [WAKE UP] TO LOAD ME UP")
    a = command().lower()
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("wake word detected")
        break
    elif (i==2 and a!=pw):
        pass

    elif (a!=pw):
        pass



def asmit():
    welcome()
    while True:
        query = command().lower()

        if "hello" in query:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + query)
            speak('Hello my boss, how can I help you?')


        elif "time" in query:
            Time = datetime.datetime.now().strftime('%I %M: %p')
            speak('It is')
            speak(Time)



        elif "remember my birthday" in query:
            speak('when is your birth day')
            query = str(input('when is your birth day: '))
            rememberMessage = query.replace("remember that ", "")
            rememberMessage = query.replace("APRIL", "")
            speak("your birth date is " + rememberMessage + " is that right")
            remember = open("jons.txt", "a")
            remember.write(rememberMessage)
            remember.close()
            query = str(input('your favor is: '))

            if 'yes' in query:
                speak("ok, i will remember")
            elif 'no' in query:
                speak('when is your birth day')
                query = str(input('when is your birth day: '))
                rememberMessage = query.replace("remember that ", "")
                rememberMessage = query.replace("APRIL", "")
                speak("your birth date is " + rememberMessage + "is that right")
                remember = open("jons.txt", "a")
                remember.write(rememberMessage)
                remember.close()
                query = str(input('your favor is: '))

            else:
                pass

        elif 'you can' in query:
            os.system('cls')
            remember = open("Remember.txt", "r")
            print(remember.read() + ' :- ' + query)
            speak('I can tell you the time and weather.')
            speak('I also can open browser or youtube.')
            speak('So, what would you like me to do now boss?')



        elif 'wikipedia' in query:
           try:
            speak("what should i search")
            person = command().lower()
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
           except:
               speak("error")

        elif 'weather' in query:
           try:
            os.system('cls')
            remember = open("Remember.txt", "r")
            print(remember.read() + ' :- ' + query)
            search = command().lower()
            url = f'https://www.google.com/search?q=temperature in {search}'
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current temperature in {search} is {temp}")
           except:
               speak("error")
        elif 'music' in query:
            speak("playing music from pc")
            music_dir = 'C:\\Users\\asmid\\Documents\\music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, musics[0]))

        elif "date" in query:
            today = datetime.datetime.now().strftime('%m')
            speak(today)
            stream.start_stream()
        elif "play a game" in query:
            from gamee import game_play
            game_play()
            if 'you_score' < 'April_score':
                speak("you won")
            elif 'you_score' > 'April_score':
                speak("i won")
            elif 'you_score' == 'April_score':
                speak("draw")
            pass

        elif 'check my internet' in query or "check my network" in query:
            internetstatus = 0
            url = "https://www.google.com/"
            timeout = 1.5
            try:
                request = requests.get(url, timeout=timeout)
                print("yes")
            except (requests.ConnectionError, requests.Timeout) as exception:
                print('no')

        elif "hi" in query:
            a5 = ["hi", "hello", "hey"]
            rand = random.choice(a5)
            speak(rand)


        elif "take a reminder " in query:
            speak('what is your new name  ')
            query = str(input('what is your new name: '))
            rememberMessage = query.replace("remember that ", "")
            rememberMessage = query.replace("APRIL", "")
            speak("your new name is asmit  " + rememberMessage)
            remember = open("jons.txt", "a")
            remember.write(rememberMessage)
            remember.close()

        elif "what is the reminder" in query:
            remember = open("jons.txt", "r")
            speak("the riminder is " + remember.read())


        elif "what is my name" in query:
            remember = open("Remember.txt", "r")
            speak("your name is " + remember.read())

        elif "change my name" in query:
            speak("alright, what should i call you")
            new_fg = input("Enter the new name:\n")
            new_detail = open("Remember.txt", "w")
            new_detail.write(new_fg)
            new_detail.close()
            speak("Done sir")
            speak(f"you'd like me to call you by the name {new_fg}. is that right")
            for i in range(3):
                p = input(" :- ")
                pw_file = open("opt.txt", "r")
                pw = pw_file.read()
                pw_file.close()
                if (p == pw):
                    speak(f"Got it . i'll call you {new_fg} from now.  ")

                    break
                elif (i == 2 and p != pw):
                    print('change it with manual settings')
                    pass

                elif (p != pw):
                    speak("alright, what should i call you")
                    new_fg = input("Enter the new name:\n")
                    new_detail = open("Remember.txt", "w")
                    new_detail.write(new_fg)
                    new_detail.close()
                    speak("Done sir")
                    speak(f"you'd like me to call you by the name {new_fg}. is that right")
        elif "month" in query:
            today = datetime.datetime.now().strftime('%m')
            stream.start_stream()
            if today == '01':
                speak("january")
            if today == '02':
                speak("february")
            if today == '03':
                speak("march")
            if today == '04':
                speak("april")
            if today == '05':
                speak("may")
            if today == '06':
                speak("june")
            if today == '07':
                speak("july")
            if today == '08':
                speak("august")
            if today == '09':
                speak("september")
            if today == '10':
                speak("october")
            if today == '11':
                speak("november")
            if today == '12':
                speak("december")


        elif "who are you" in query:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + query)
            speak('Hi, I am your virtual assistant. How can I help you now, sir?')
            stream.start_stream()





        elif "who made you" in query:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + query)
            speak('asmit created me. Is there something else you need me to help you with?')
            stream.start_stream()


        elif "who make you" in query:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + query)
            speak('asmit created me. Is there something else you need me to help you with?')
            stream.start_stream()


        elif "who created you" in query:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + query)
            speak('asmit created me. Is there something else you need me to help you with?')
            stream.start_stream()






        elif "add" in query:
            speak("first number")
            first_number = command().lower()
            speak("second_number")
            second_number = input("enter second number:")
            result = str(float(first_number) + float(second_number))
            speak(result)

        elif "subtract" in query:
            speak("first number")
            first_number = command().lower()
            speak("second number")
            second_number = command().lower()
            result = str(float(first_number) - float(second_number))
            speak(result)
        elif "multiply" in query:
            speak("first number")
            first_number = command().lower()
            speak("second number")
            second_number = command().lower()
            result = str(float(first_number) * float(second_number))
            speak(result)

        elif "divide" in query:
            speak("first number")
            first_number = command().lower()
            speak("second number")
            second_number = command().lower()
            result = str(float(first_number) / float(second_number))
            speak(result)

        elif "who create you" in query:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + query)
            speak('asmit created me.')
            stream.start_stream()


        elif "where are you from" in query:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + query)
            speak('i am from India')
            stream.start_stream()





        elif "stop" in query or "quit" in query:
            speak("Assistant is off. Goodbye sir")
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load('fg.mp3')
            pygame.mixer.music.play()
            sleep(2)
            quit()

        elif "joke" in query:
            a42 = speak(pyjokes.get_joke())
            print(a42)





        elif "near earth objects" in query:
            print('Recognized text: ' + query)
            speak(f'connecting to NASA')
            try:
                from Nasa import Astro
                speak("tell me the starting date sir!")
                start = input("Enter the starting date :")
                speak("tell me the end date.")
                end = input("Enter the ending date :")
                Astro(start, end)
                Astro()
            except:
                speak("Can't connect to NASA's computer")
                print("")
        elif 'track iss' in query:
            speak(f'connecting to NASA')
            try:
                from Nasa import IssTracker

                IssTracker()
            except:
                speak("Can't connect to NASA's computer")
                print("")



        elif "google" in query:

            try:
             import pywhatkit
             speak("what should i search")
             query = command().lower()
             speak("would you like to see the page")
             coomand = command().lower()
             if "yes" in coomand:
                 speak("this is what i found")

                 try:
                     pywhatkit.search(query)
                     result = googleScrap.summary(query, 3)
                     speak(result)

                 except:
                     speak("no speakable data")

             elif "no" in coomand:
                 speak("this is what i found")

                 try:

                     result = googleScrap.summary(query, 3)
                     speak(result)

                 except:
                     speak("no speakable data")
             else:
                 speak("this is what i found")

                 try:
                     pywhatkit.search(query)
                     result = googleScrap.summary(query, 3)
                     speak(result)

                 except:
                     speak("no speakable data")
            except:
                speak("error")

        elif 'good night' in query:
            speak(
                'good night sir. can i also go to sleep now ')
            print('☺')
            query = str(input('your favor is: '))
            if ('yes') in query:
                print('thank you')
                speak('thank you')
                exit()

            elif ('no') in query:
                pass

            else:
                speak(
                    'can i also go to sleep now ')
                print('☺')
                query = str(input('your favor is: '))
                if ('yes') in query:
                    print('thank you')
                    speak('thank you')
                    exit()

                elif ('no') in query:
                    pass
        elif "youtube" in query:
           try:
            os.system('cls')
            remember = open("Remember.txt", "r")
            print(remember.read() + ' :- ' + query)
            speak('What should I search on youtube now boss?')
            search = command().lower()
            url = f'https://youtube.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Youtube for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')

            speak(f'what else you would like me to do, boss?')
           except:
               speak("error")

        else:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text:' + query)
            print(".....")
            pass
            stream.start_stream()

if __name__ == '__main__':
 asmit()
