from fastapi import FastAPI
from fastapi.responses import FileResponse
from gtts import gTTS
import os

app = FastAPI()

# Define available languages and accents (these are just examples)
available_languages = {
    "en_us": "en",  # English (US)
    "en_uk": "en",  # English (UK)
    "es": "es",     # Spanish
    "fr": "fr",     # French
    "de": "de"      # German
}

@app.get("/text-to-speech")
async def text_to_speech(text: str, lang: str = "en_us"):
    """
    Convert text to speech and return the audio file with different language/accent options.
    
    :param text: The text to convert into speech.
    :param lang: The language code for the speech. Defaults to "en_us".
    :return: Audio file of the spoken text.
    """
    if lang not in available_languages:
        return {"error": f"Language '{lang}' not supported. Available options: {', '.join(available_languages.keys())}"}

    # Use gTTS to convert text to speech
    tts = gTTS(text=text, lang=available_languages[lang])
    audio_filename = "output.mp3"
    tts.save(audio_filename)
    
    # Return the audio file as a response
    return FileResponse(audio_filename, media_type='audio/mp3', filename=audio_filename)

@app.on_event("shutdown")
def shutdown_event():
    # Cleanup: Remove temporary file
    if os.path.exists("output.mp3"):
        os.remove("output.mp3")