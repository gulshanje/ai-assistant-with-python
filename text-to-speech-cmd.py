import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty('rate')
print(f'Current rate: {rate}')
engine.setProperty('rate', 180)

volume = engine.getProperty('volume')
print(f'Current volume: {volume}')
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
print(f'Available voices: {voices}')
engine.setProperty('voice', voices[1].id)
engine.say("Hello, I am an AI assistant. I will guide you through a simple text-based game.")
engine.runAndWait()