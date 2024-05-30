from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3", lang="english", slow=0):
    #intialise of gTTS with text
    tts = gTTS(text=text, lang=lang, slow=slow)

    #to save audio file
    tts.save(filename)

    #to play audio file
    os.system("start" + filename)

if __name__ == "__main__":
    user_input = input("Enter the text to convert to speech: ")
    lang = input("Enter the language (default is English): ")
    slow = input("Do you want the speech to be slow? (y/n): ").lower() == 'y'
    filename = input("Enter the filename to save the speech (default is output.mp3): ")

    text_to_speech(user_input, filename, lang, slow)