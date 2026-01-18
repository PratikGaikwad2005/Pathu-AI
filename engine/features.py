import re
from engine.config import ASSISTANT_NAME
from playsound import playsound
import eel
import os
from engine.command import speak
import pywhatkit as kit

# function to play start sound
def playAssistantSound():
    music_dir = "www\\assets\\audio\\pathu_start_sound.mp3"
    playsound(music_dir)
 
# This eel.expose is used to use playClickSound function in javascript file  
@eel.expose
# function to play click sound
def playClickSound():
    music_dir = "www\\assets\\audio\\pathu_click_sound.mp3"
    playsound(music_dir)
    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME , "")
    query = query.replace('open',"")    
    
    query.lower()
    
    if query != "":
        speak("Opening" + query)
        os.system('start' +query)
    else:
        speak(f"{query} not found")
        
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Sorry , I couldn't find the term to play on YouTube..")
        
def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern , command ,re.IGNORECASE)
    return match.group(1) if match else None