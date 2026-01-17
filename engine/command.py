import pyttsx3
import speech_recognition as sr
import eel


# speak function 
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty('rate',170)
    engine.runAndWait()
    
#conver speech to text function
@eel.expose
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1                        # Adjust pause threshold for better recongition
        r.adjust_for_ambient_noise(source)           #Adjust for ambient noise
        audio = r.listen(source , timeout=10 , phrase_time_limit=5)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language = 'en')
        print(f'User said: {query}')
        speak(query)
    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query.lower()

# text = speech_to_text()

# speak(text)