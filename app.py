import os
import eel
from engine.features import *
from engine.command import *

# This are the eel commands to start the application on notepad
eel.init('www')

# call the function to play assistant start sound from emgine/features.py
playAssistantSound()

os.system('start chrome.exe --app="http://localhost:8000/index.html"')
eel.start('index.html' , mode = 'chrome' , host='localhost' , block=True)
