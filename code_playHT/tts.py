import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from pyht import Client
from pyht.client import TTSOptions
import tempfile

# Load environment variables
load_dotenv()

# Retrieve PlayHT credentials from .env
USER_ID = os.getenv("PLAY_HT_USER_ID")
API_KEY = os.getenv("PLAY_HT_API_KEY")

# Initialize PlayHT client
client = Client(user_id=USER_ID, api_key=API_KEY)

# Initialize FastAPI app
app = FastAPI()

@app.get("/text-to-speech")
async def text_to_speech(text: str, voice_id: str = "s3://voice-cloning-zero-shot/775ae416-49bb-4fb6-bd45-740f205d20a1/jennifersaad/manifest.json"):
    """
    Convert text to speech using PlayHT's PlayDialog engine and return the audio file.
    
    :param text: The text to be converted into speech.
    :param voice_id: The PlayHT voice ID (must start with s3://). Defaults to Jennifer.
    :return: Audio file of the spoken text.
    """
    # Ensure the voice_id starts with s3://
    if not voice_id.startswith("s3://"):
        raise HTTPException(status_code=400, detail="Invalid voice_id format. It should start with 's3://'.")
    
    try:
        # Set the TTS options with the provided voice_id
        options = TTSOptions(voice=voice_id)
        
        # Generate the audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            # Use PlayHT SDK to generate speech and write it to the file
            for chunk in client.tts(text, options, voice_engine="PlayDialog", protocol="http"):
                temp_file.write(chunk)
        
            # Return the audio file as a response
            return FileResponse(temp_file.name, media_type="audio/wav", filename="output_jenn.wav")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")