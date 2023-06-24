import pyttsx3
import speech_recognition 
import datetime
from tkinter import *

root=Tk()
engine = pyttsx3.init("nsss")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)
   
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,6)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def project():
    query = takeCommand().lower()
    if "wake up" in query:
        from GreetMe import greetMe
        greetMe()

        while True:
            query = takeCommand().lower()
            if "finally sleep" in query:
                speak("Going to sleep,sir")
                exit()
                    
            elif "calculate" in query:
                from calculatenum import WolfRamAlpha
                from calculatenum import Calc
                query = query.replace("calculate","")
                Calc(query)
                
         

def myclick():
    myLabel=Label(root,text="Calculator is Active")
    myLabel.pack()

login_btn = PhotoImage(file='/Users/rishav/Desktop/Aiproject/microphone.png')    
img_label = Label(image=login_btn)

def o_and_t():
    project()
    myclick()

myLabel1=Label(root,text="Voice Calculator") 
myLabel1.pack()  
      
myButton=Button(root, image=login_btn, command=o_and_t)
myButton.pack()


root.mainloop()                
