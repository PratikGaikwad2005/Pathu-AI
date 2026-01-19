import re
import sqlite3
import webbrowser
from engine.config import ASSISTANT_NAME
from playsound import playsound
import eel
import os
from engine.command import speak
import pywhatkit as kit


conn = sqlite3.connect('pathuDB.db')

cursor = conn.cursor()


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
    
    
# function to open application or webapp based on database entries
def openCommand(query):
    query = query.replace(ASSISTANT_NAME , "")
    query = query.replace('open',"").strip().lower()    
    
    
    if query != "":
        try:
            # Try to find the application in sys_command table
            cursor.execute('SELECT path FROM sys_command WHERE LOWER(name) = ?', (query,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])
                return

            # If not found, try to find the URL in web_command table
            cursor.execute('SELECT url FROM web_command WHERE LOWER(name) = ?', (query,))
            results = cursor.fetchall()
            
            if len(results) != 0:
                speak("Opening " + query)
                webbrowser.open(results[0][0])
                return

            # If still not found, try to open using os.system
            speak("Opening " + query)
            try:
                os.system('start ' + query)
            except Exception as e:
                speak(f"Unable to open {query}. Error: {str(e)}")

        except Exception as e:
            speak(f"Something went wrong: {str(e)}")
        
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