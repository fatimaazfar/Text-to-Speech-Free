from gtts import gTTS

# List available languages in gTTS
languages = gTTS.get_languages()

# Print the available languages and their codes
print("Available Languages and Codes in gTTS:")
for lang_code, lang_name in languages.items():
    print(f"{lang_code}: {lang_name}")
