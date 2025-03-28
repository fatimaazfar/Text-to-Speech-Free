### Text-to-Speech (TTS) API Documentation

This document provides detailed information on three different Text-to-Speech (TTS) endpoints created using FastAPI, utilizing three TTS libraries: **Pyttsx3**, **gTTS**, and **PlayHT**.

---

### 1) **Pyttsx3-based TTS Endpoint (Free)**

#### Endpoint:
`GET /text-to-speech`

#### Description:
This endpoint converts the provided text into speech using the **pyttsx3** library, which is a text-to-speech conversion library in Python. The speech is generated based on a selected voice and returned as an audio file (MP3 format).

#### Query Parameters:
- **`text`** (string, required): The text to be converted to speech.
- **`voice_id`** (integer, optional): The ID of the voice to use (default: `1`). Voice ID corresponds to available voices in the pyttsx3 engine. Voice IDs are typically 0 for male and 1 for female voices, but this may vary.

#### Example Request:
```
GET /text-to-speech?text=Hello%20World&voice_id=1
```

#### Response:
- **200 OK**: A `.mp3` file containing the speech.
  - **Content-Type**: `audio/mp3`
  - **Filename**: `output.mp3`
  
- **400 Bad Request**: If the provided `voice_id` is invalid.
  - Example: 
    ```json
    {
      "error": "Invalid voice ID."
    }
    ```

#### Usage:
- The API will check if the provided `voice_id` is valid based on the list of voices in pyttsx3. If the ID is valid, the speech will be generated and returned as a downloadable MP3 file.
- The temporary file (`output.mp3`) is automatically deleted upon shutdown.

---

### 2) **gTTS-based TTS Endpoint (Free)**

#### Endpoint:
`GET /text-to-speech`

#### Description:
This endpoint converts the provided text into speech using the **gTTS** (Google Text-to-Speech) library. It supports various languages and accents for speech generation.

#### Query Parameters:
- **`text`** (string, required): The text to be converted to speech.
- **`lang`** (string, optional): The language code to be used for speech. Defaults to `"en_us"`. Available language codes include:
  - `"en_us"`: English (US)
  - `"en_uk"`: English (UK)
  - `"es"`: Spanish
  - `"fr"`: French
  - `"de"`: German
  
#### Example Request:
```
GET /text-to-speech?text=Hola%20Mundo&lang=es
```

#### Response:
- **200 OK**: A `.mp3` file containing the speech.
  - **Content-Type**: `audio/mp3`
  - **Filename**: `output.mp3`
  
- **400 Bad Request**: If the provided `lang` parameter is not supported.
  - Example: 
    ```json
    {
      "error": "Language 'de_us' not supported. Available options: en_us, en_uk, es, fr, de"
    }
    ```

#### Usage:
- The API will check if the provided `lang` is supported. If supported, it generates speech using gTTS and returns the MP3 file.
- The temporary file (`output.mp3`) is automatically deleted upon shutdown.

---

### 3) **PlayHT-based TTS Endpoint (Paid)**

#### Endpoint:
`GET /text-to-speech`

#### Description:
This endpoint converts the provided text into speech using **PlayHT**, a high-quality TTS service. The speech is generated using a PlayHT voice ID and returned as an audio file (WAV format).

#### Query Parameters:
- **`text`** (string, required): The text to be converted to speech.
- **`voice_id`** (string, optional): The PlayHT voice ID (default: `s3://voice-cloning-zero-shot/775ae416-49bb-4fb6-bd45-740f205d20a1/jennifersaad/manifest.json`). The voice ID should start with `s3://` to indicate a PlayHT-compatible voice.

#### Example Request:
```
GET /text-to-speech?text=Hello%20PlayHT&voice_id=s3://voice-cloning-zero-shot/775ae416-49bb-4fb6-bd45-740f205d20a1/jennifersaad/manifest.json
```

#### Response:
- **200 OK**: A `.wav` file containing the speech.
  - **Content-Type**: `audio/wav`
  - **Filename**: `output_jenn.wav`

- **400 Bad Request**: If the provided `voice_id` does not start with `s3://`.
  - Example:
    ```json
    {
      "detail": "Invalid voice_id format. It should start with 's3://'."
    }
    ```

- **500 Internal Server Error**: If there is any error with generating the speech.
  - Example:
    ```json
    {
      "detail": "An error occurred: [error_message]"
    }
    ```

#### Usage:
- The API ensures that the `voice_id` starts with `s3://`, which is the required format for PlayHT's voice IDs.
- It uses PlayHT’s SDK to generate the audio and returns the resulting `.wav` file.
- The temporary file is stored in a non-volatile location and deleted when the process is finished.

---

### General Notes for All Endpoints:

- **Security**: Ensure that any API keys or sensitive data are properly stored in environment variables and not hardcoded in the code.
- **File Cleanup**: All endpoints clean up temporary files after the API shuts down, so no unnecessary files are left on the server.
- **Error Handling**: The API returns relevant error messages when input parameters are incorrect or unsupported, ensuring the user knows how to correct them.

---

By using these endpoints, users can easily convert any text to speech with a variety of languages, accents, and voices, all while receiving the output as a downloadable audio file for further use.
