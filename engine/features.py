from playsound import playsound
import eel

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