import pyttsx3

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Print available voices and their IDs
for idx, voice in enumerate(voices):
    print(f"Voice ID: {idx} - Name: {voice.name}, Lang: {voice.languages}")