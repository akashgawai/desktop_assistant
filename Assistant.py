import random
import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import datetime
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # Without this command, speech will not be audible to us.


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
         speak("Good Morning!")
    elif hour >= 12 and hour < 18:
         speak("Good Afternoon!")
    else:
         speak("Good Evening!")
    speak("Hello Akash. I am your assistant. How may I help you")


def takeCommand():  # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.
    except Exception as e:
        speak("I cant recognize please say again...")
        print("I cant recognize please say again...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        #if 1:
            query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
            if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                
            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'email' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "xyz@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")

            elif 'play song' in query:
                music_dir = 'D:\\Song\\unpluged'
                songs = os.listdir(music_dir)
                n = random.randint(0, 110)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[n]))
                
            elif 'open chrome' in query:
                codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)