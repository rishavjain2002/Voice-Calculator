import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("nsss")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def WolfRamAlpha(query):
    apikey = "27AEP5-3LP6QEXQGV"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")
        return 0

def Calc(query):
    Term = str(query)
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak("The answer is")
        speak(result)
        
    except:
        speak("The value is not answerable")
    #return result

