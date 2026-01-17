import pyttsx3
import speech_recognition as sr
import eel


# speak function 
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #print(voices)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    
#conver speech to text function
@eel.expose
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1                        # Adjust pause threshold for better recongition
        r.adjust_for_ambient_noise(source)           #Adjust for ambient noise
        audio = r.listen(source , timeout=10 , phrase_time_limit=5)
        
    try:
        print("Recognizing...")
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio , language = 'en')
        print(f'User said: {query}')
        speak(query)
        
        eel.DisplayMessage(query)                  # This function displayMessage is use to display the message on fron end whoes function is defined in controller.js
        eel.ShowHood()
    
    except Exception as e:
        print("Say that again please...")
        eel.DisplayMessage('Please Say it onces more...')
        return "None"
    
    return query.lower()

# text = speech_to_text()

# speak(text)

@eel.expose
def allCommands():
    query = speech_to_text()
    print(query)
    
    if 'open' in query:
        print('is running')
    else:
        print('not running')