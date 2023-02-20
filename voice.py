import pyttsx3                     #text-to-speech conversion library
import speech_recognition as sr    #Library for performing speech recognition
import webbrowser                  #displaying web-based documents to users
import datetime                    #supplies classes for manipulating dates and times.
import pyjokes                     #used to create one-line jokes for programmers


#function to convert speech to text
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphonr() as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)           #cancelling noise
        audio=recognizer.listen(source)                       #it will listen to the source
        try:
            print("Recognizing.....")
            data=recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Not Understanding")

# def speechtx(x):
#     engine=pyttsx3.init()
#     voices=engine.getProperty('voices')
#     engine.setProperty('voice',voices[0].id)         #0->male, 1->female
#     rate=engine.getProperty('rate')
#     engine.setProperty('rate',150)
#     engine.say(x)
#     engine.runAndWait()
    
    
# speechtx("Hello")       
#sptext()
        