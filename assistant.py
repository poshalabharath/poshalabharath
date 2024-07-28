import pyttsx3  # type: ignore # pip install pyttsx3
import speech_recognition as sr  # type: ignore # pip install speechRecognition
import datetime
import wikipedia  # type: ignore # pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio # type: ignore



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)#voice[0]-male voice[1]-female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am VA Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("from_mail_id", "password")
    server.sendmail("from_mail_id", to, content)
    server.close()    

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stack overflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")


        elif 'play music' in query:
            music_dir ="C:\\Users\\posha\\Music"  # your music playlist location path
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\posha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #your code location
            os.startfile(codePath)
            
        elif 'open photo' in query:
            photoPath = "C:\\Users\\posha\\OneDrive\\Pictures\\my photo.jpg" # your photo location
            os.startfile(photoPath)

            

        elif 'email to friend' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "poshalabharath241@gmail.com" #for example :bharath@gmail.com
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")
                
        