import pyttsx3                     #text-to-speech conversion library
import speech_recognition as sr    #Library for performing speech recognition
import webbrowser                  #displaying web-based documents to users
import datetime                    #supplies classes for manipulating dates and times.
import pyjokes                     #used to create one-line jokes for programmers
import time
import ctypes
import subprocess
import winshell

#function to convert speech to text
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)           #cancelling noise
        audio=recognizer.listen(source)                       #it will listen to the source
        try:
            print("Recognizing.....")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understanding")

def txtsp(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)         #0->male, 1->female
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
    
#splitting the function
if __name__=='__main__':

        
    if "peter" in sptext().lower():    #activating the system
        while True:
            data1=sptext().lower()
            
            if "your name" in data1:
                name="my name is peter"
                txtsp(name)

            elif "old are you" in data1:
                txtsp("I am two years old")

            elif "now time" in data1:
                time=datetime.datetime.now().strftime("%I%M%p")     #%M->minute, %p->AM/PM, %I->hours
                txtsp(time)

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif 'news' in data1:
                webbrowser.open("https://www.google.com/search?q=latest+news&rlz=1C1CHWL_enIN991IN991&sxsrf=AJOqlzU9idgROmrxUz1WEq0akDaJnwfoCg%3A1676630932954&ei=lFvvY_HxObG73LUP_-e8oAk&ved=0ahUKEwjxi7b5sJz9AhWxHbcAHf8zD5QQ4dUDCA8&uact=5&oq=latest+news&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIECAAQQzIKCAAQsQMQgwEQQzIECAAQQzIECAAQQzIECAAQQzITCAAQgAQQFBCHAhCxAxCDARDJAzINCAAQgAQQFBCHAhCxAzoKCAAQRxDWBBCwAzoICAAQkgMQsAM6CgguELEDEIMBEEM6BQgAEIAEOgsIABCABBCxAxCDAToHCAAQsQMQQzoHCAAQgAQQCjoHCC4QgAQQCkoECEEYAFC9BFjhJWDgJ2gCcAF4AIABogaIAa4XkgEFNS0xLjOYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp")

            elif 'joke' in data1:
                joke_1=pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                txtsp(joke_1)

            elif 'play song' in data1:
                webbrowser.open("https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")
                
            elif 'is love' in data1:
                txtsp("It is 7th sense that destroy all other senses")
 
            elif "who are you" in data1:
                txtsp("I am your virtual assistant created by Pragya")
                
            elif 'lock window' in data1:
                txtsp("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
            elif 'shutdown system' in data1:
                txtsp("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
            elif 'empty recycle bin' in data1:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                txtsp("Recycle Bin Recycled")
                
            elif 'how are you' in data1:
                txtsp("I am fine, Thank you")
                txtsp("How are you, Sir")
 
            elif 'fine' in data1 or "good" in data1:
                txtsp("It's good to know that your fine")

            elif "exit" in data1:
                txtsp("Thank You")
                break
            else:
                print("Thanks")
                
            time.sleep(5)