import requests

# Define the FastAPI endpoint
API_URL = "http://127.0.0.1:8000/text-to-speech"

# Example text to convert to speech
text = "Congratulations on joining SecurityPro Group! As a leading provider of security solutions and an ADT authorized dealer, we take pride in offering our customers the best in home and business security. But just as importantly, we invest in our team, because you are the foundation of our success. This course will provide you with comprehensive training to ensure you master security system design, sales techniques, and customer service best practices. Our mentorship programs pair you with experienced professionals to help you succeed from day one. Ongoing coaching and support keep you at the top of your game in a competitive market. We offer top commission and volume bonuses, putting your earnings potential in the palm of your hand. With our strong multi channel marketing, you’ll always have opportunities to earn big commissions. As an ADT authorized dealer we offer customers the latest in ADT smart home security, including: Remote control of their security system from a smartphone anywhere they have signal. Add ons include smart locks, cameras, thermostats and home automation. All with 24 7 professional monitoring. With our immersive training you will stay ahead of the curve in the fast-growing home security industry. You’ve joined a supportive and motivated team that pushes each other to succeed. Our culture is built on integrity, professionalism, and teamwork. We win together. Keep in mind, you’re not just selling a product, you are protecting families, businesses, and communities. Every installation you sell, provides peace of mind to customers. Your work makes homes safer and helps businesses reduce risks."

# Example voice ID (use a valid PlayHT voice URL)
voice_id = "s3://voice-cloning-zero-shot/775ae416-49bb-4fb6-bd45-740f205d20a1/jennifersaad/manifest.json"

# Set up parameters for the GET request
params = {
    "text": text,
    "voice_id": voice_id
}

# Send GET request to the FastAPI endpoint
response = requests.get(API_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Save the audio file locally
    with open("output_playht.wav", "wb") as audio_file:
        audio_file.write(response.content)
    print("Audio file saved as 'output_playht.wav'")
else:
    print(f"Failed to generate speech. Status code: {response.status_code}")
    print(f"Response: {response.text}")