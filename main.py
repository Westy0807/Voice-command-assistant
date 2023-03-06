#Please pip-install/interface-install these before use or nothing will work!
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


#Setting up Alexa/anything you wanna call it!!! RAHHHH 
listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#What happens when talk
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_commad():
    try:
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "doug" in command:#rename as anything of liking other than doug
                command = command.replace("doug"," ")#change to the name you want it to use(Telling it when it takes commands to not look at doug)
                print(command)


    except:
        pass
    return command
#All fetures curently
def run_alexa():
    #Song
    command = take_commad()
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
     #Time
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("The time is " + time)
     #person look up thingy
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)
       #Search for anything on chrome
    elif "search for" in command:
        targetsc = command.replace("search for", "")
        targetsc = command
        pywhatkit.search(targetsc)
        talk("Here are the results for" + targetsc)
        print(targetsc)
        #ask about its day(codes have feeling toooooooo)
    elif "your day" in command:
        talk("My day is going great")
        print("my day is going great")
        #MAKE it telll you a joke
    elif "joke" in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
        #weather
    elif "weather " in command:
        targetsc = command
        command = command.replace("what is", "")
        pywhatkit.search(targetsc)
        talk("This is what the" + command)
        print(command)
        #weather tommorow if you really wanted to know
    elif "weather tommorow " in command:
        targetsc = command
        pywhatkit.search(targetsc)
        talk("This is what the" + command)
        print(command)
        #same assearch for but for those who cant remeber
    elif "look for" in command:
        targetsc = command.replace("look for", "")
        targetsc = command
        pywhatkit.search(targetsc)
        talk("Here are the results for" + targetsc)
        print(targetsc)









run_alexa()

