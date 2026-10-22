# Jarvis Voice Assistant

A Python-based voice assistant that recognizes voice commands, opens websites, plays music, reads news, and answers questions using Cohere AI.

## Features

- **Voice Recognition:** Listens for the wake word "Jarvis" and processes voice commands.
- **Website Automation:** Opens Google, Facebook, YouTube, and LinkedIn.
- **Music Playback:** Plays songs using a configurable YouTube music library.
- **News Updates:** Fetches and reads Indian headlines using NewsAPI.
- **AI Conversations:** Uses Cohere AI to answer user questions.
- **Speech Output:** Responds using text-to-speech.

## Tech Stack

- Python
- Cohere API
- NewsAPI
- SpeechRecognition
- pyttsx3
- gTTS
- Pygame
- Requests
- python-dotenv

## Requirements

- Python 3.10 or higher
- Working microphone and speakers
- Internet connection

## Installation

1. Clone the repository:

   ```bash
   git clone <your-github-repository-url>
   cd jarvis-voice-assistant
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## API Configuration

Create a `.env` file in the project root and add your API keys:

```env
COHERE_API_KEY=your_cohere_api_key
NEWSAPI_KEY=your_newsapi_api_key
```

The application loads these variables using `python-dotenv`.

- [Cohere Dashboard](https://dashboard.cohere.com/)
- [NewsAPI](https://newsapi.org/)

**Security:** Never commit `.env` or expose API keys in your source code or GitHub repository. Keep `.env` in `.gitignore` and use `.env.example` with placeholder values.

## Run the Application

```bash
python main.py
```

Say **"Jarvis"** to activate the assistant, then speak a command.

Example commands:
- "Open Google"
- "Open YouTube"
- "Play [song name]"
- "What is coding?"
- "News"

## Music Library

Add or update songs in `musicLibrary.py` using song names and their corresponding YouTube URLs.

## Project Structure

```text
jarvis-voice-assistant/
├── main.py
├── musicLibrary.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

This structure is illustrative. Keep it consistent with the files actually present in your repository.
