import requests

# URL of your FastAPI endpoint
url = "http://127.0.0.1:8000/text-to-speech"

# Parameters for the request
params = {
    "text": "Hello, this is a test of the text to speech API.",
    "lang": "es"  # You can change this to test different languages/accent options (e.g., "en_uk", "es", "fr", "de")
}

# Send a GET request to the API endpoint
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Save the audio file
    with open("output_es.mp3", "wb") as file:
        file.write(response.content)
    print("Audio file saved as 'output.mp3'")
else:
    print(f"Failed to get audio. Status code: {response.status_code}")