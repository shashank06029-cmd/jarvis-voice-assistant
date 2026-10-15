import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os
import cohere
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init() 

# 🔹 API Keys from environment variables (DO NOT HARDCODE!)
NEWSAPI = os.getenv("NEWSAPI_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Validate that API keys are configured
if not NEWSAPI:
    raise ValueError("NEWSAPI_KEY not found in environment variables. Please set it in your .env file.")
if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY not found in environment variables. Please set it in your .env file.")

co = cohere.Client(COHERE_API_KEY)

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

# Initialize pygame mixer once at module level
pygame.mixer.init()

def speak(text):
    try:
        tts = gTTS(text)
        tts.save('temp.mp3') 

        pygame.mixer.music.load('temp.mp3')
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        pygame.mixer.music.unload()
        os.remove("temp.mp3")
    except Exception as e:
        print(f"Error in speak function: {e}")

# ==============================
# 🔹 Cohere AI function
# ==============================
def aiProcessCohere(command):
    try:
        response = co.chat(
            model="command-r-08-2024",   # Updated model
            message=f"You are Jarvis, a helpful AI voice assistant. Respond briefly and clearly.\nUser: {command}"
        )
        return response.text.strip()
    except Exception as e:
        print("Error while connecting to Cohere:", e)
        return "Sorry, I couldn’t process your request."

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWSAPI}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])

    else:
            output = aiProcessCohere(c)
            speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
                    print(f"Error: {e}")
