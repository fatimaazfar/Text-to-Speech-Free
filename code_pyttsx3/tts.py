from fastapi import FastAPI
from fastapi.responses import FileResponse
import pyttsx3
import os

app = FastAPI()

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# List available voices (you can choose from these)
voices = engine.getProperty('voices')

@app.get("/text-to-speech")
async def text_to_speech(text: str, voice_id: int = 1):
    """
    Convert text to speech and return the audio file.
    
    :param text: The text to convert into speech.
    :param voice_id: The ID of the voice to use. Defaults to 1.
    :return: Audio file of the spoken text.
    """
    if voice_id < 0 or voice_id >= len(voices):
        return {"error": "Invalid voice ID."}

    # Set the selected voice
    engine.setProperty('voice', voices[voice_id].id)

    # Create a temporary file to save the audio
    audio_filename = "output.mp3"
    engine.save_to_file(text, audio_filename)
    
    # Run the engine to generate speech
    engine.runAndWait()

    # Return the audio file as a response
    return FileResponse(audio_filename, media_type='audio/mp3', filename=audio_filename)

@app.on_event("shutdown")
def shutdown_event():
    # Cleanup: Remove temporary file
    if os.path.exists("output.mp3"):
        os.remove("output.mp3")