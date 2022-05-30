import subprocess
from click import command
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import webbrowser







listener=sr.Recognizer()
engine=pyttsx3.init('espeak')
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)
engine.say('Bixby one point O')
engine.say('I am your assistant.')
engine.say('How may I help you?')
engine.runAndWait()


def speak_command_by_assistant_user_give(text):
    engine.say(text)
    engine.runAndWait()




 
def bixby_command():
    try:
            with sr.Microphone() as source:
                print('Listening....')
                voice=listener.listen(source)
                print('Recognizing...')
                command=listener.recognize_google(voice)
                command=command.lower()
                
            if "bixby" in command:
                print('Input : '+ command)
    except:
            pass
    return command


def run_bixby():
    command=bixby_command()
    
    if "play"  in command:
        if "bixby" in command:
            song=command.replace("play","")
            speak_command_by_assistant_user_give("Playing"+song)
            print('Output:'+song)
            pywhatkit.playonyt('Output :' + song)

    elif "time" in command:
        if "bixby" in command:
            time=datetime.datetime.now().strftime("%H:%M")
            print('Output : '+ time)
            speak_command_by_assistant_user_give("Current time is"+time)

    elif "joke" in command:
        if "bixby" in command:
            a=command.replace("joke","")
            print('Output:'+a)
            speak_command_by_assistant_user_give('Joke  is here '+ pyjokes.get_joke())

    elif "search" in command:
        if "bixby" in command:
        
            url='https://www.google.co.in/search?q='+command
            a=command.replace("search","")
            print('Output : '+a)
            webbrowser.open(url)
            speak_command_by_assistant_user_give('Searching result')
    
   
    elif "how are you " in command:
        if "bixby" in command:
            speak_command_by_assistant_user_give('I am good')
            speak_command_by_assistant_user_give('How are you sir')

    elif "fine" in command:
        speak_command_by_assistant_user_give('Thats good sir.')



    elif "open youtube" in command:
        if "bixby" in command:
            speak_command_by_assistant_user_give("Here you go to Youtube \n")
            webbrowser.open("https://www.youtube.com/")

     
    elif "who are you" in command:
        speak_command_by_assistant_user_give('I am your assistant.')

    
    elif "who i am " in command:
        if "bixby" in command:
            speak_command_by_assistant_user_give('You are not a robot.')
    
    elif "shutdown" in command:
        if "bixby" in command:
            speak_command_by_assistant_user_give('Please save the work and close the items before using this process.')
            subprocess.call(['shutdown'])
    elif "restart" in command:
        if "bixby" in command:
            speak_command_by_assistant_user_give('Restarting')
            subprocess.call(["shutdown","/r"])
    
    elif "location" in command:
        if "bixby" in command:
            a=command.replace("location")
            print('Output :'+a)
            speak_command_by_assistant_user_give('Your location is Delhi')
    
    elif "call" in command:
        if "bixby" in command:
            a=command.replace("call","")
            print('Output : ',a)
            speak_command_by_assistant_user_give('Calling Please Wait a minute.')

run_bixby()