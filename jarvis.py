import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import os
import smtplib


 
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am you Voice Assistant how may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

 
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtp.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results.encode("utf-8"))
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Anish\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open spotify' in query:
            codePath = "C:\\Users\\Anish\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)
 
        # elif 'play music' in query:                                        For playing song from a directory in the PC
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     os.startfile(os.path.join(music_dir, songs[0]))
        

        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'open youtube' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe" 
            os.startfile(codePath)

        elif 'quit' in query:
            exit()
            

        elif 'email to anish' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "anishyouremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, My friend I am not able to send this Email.")
        

 

 