from library import *
def speak(tool):
    
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',150)
    engine.say(tool)
    engine.runAndWait() 