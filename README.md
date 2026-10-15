# Jarvis Voice Assistant

A Python-based voice assistant using Cohere AI for natural language processing.

## Features

- Voice recognition and speech synthesis
- Web browser automation (Google, Facebook, YouTube, LinkedIn)
- Music playback from YouTube
- News reading from NewsAPI
- AI-powered conversations using Cohere AI

## Prerequisites

- Python 3.10 or higher
- Microphone for voice input
- Internet connection

## Installation

1. **Activate the virtual environment:**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

## How to Run

1. **Activate the virtual environment:**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

2. **Run the main script:**
   ```powershell
   python main.py
   ```

## Usage

1. Say "Jarvis" to activate the assistant
2. Speak your command after hearing "Ya"
3. Examples:
   - "Open Google"
   - "Open YouTube"
   - "Play apk" (plays a song from your music library)
   - "What is coding?" (AI conversation)
   - "News" (reads latest news)

## Music Library

Edit [musicLibrary.py](file://c:\Users\Shashank%20Shekhar\OneDrive\Desktop\python-project\mega_01p%20jarvis\musicLibrary.py) to add your own songs:

```python
music = {
    "songname": "youtube_url",
    # Add more songs...
}
```

## Configuration

### 🔐 API Keys Setup (REQUIRED)

This project uses environment variables to store API keys securely. **Never commit API keys to Git!**

1. **Copy the example environment file:**
   ```powershell
   copy .env.example .env
   ```

2. **Edit `.env` and add your API keys:**
   ```
   COHERE_API_KEY=your_actual_cohere_api_key
   NEWSAPI_KEY=your_actual_newsapi_key
   ```

3. **Get your API keys:**
   - Cohere: https://dashboard.cohere.com/
   - NewsAPI: https://newsapi.org/

⚠️ **IMPORTANT:** The `.env` file is in `.gitignore` and should NEVER be committed to Git.

### Security Best Practices

- **Rotate your API keys** if they were previously exposed in Git history
- Use different keys for development and production
- Never share your `.env` file
- Consider using a secrets manager for production deployments

## Troubleshooting

### Microphone Issues
- Ensure your microphone is properly connected
- Check Windows sound settings and grant microphone permissions

### Audio Playback Issues
- Ensure pygame mixer is properly initialized
- Check that your audio output device is working

### Voice Recognition Issues
- Speak clearly and at a moderate volume
- Ensure internet connection is active (Google Speech Recognition requires internet)

## Files

- [main.py](file://c:\Users\Shashank%20Shekhar\OneDrive\Desktop\python-project\mega_01p%20jarvis\main.py) - Main application entry point
- [musicLibrary.py](file://c:\Users\Shashank%20Shekhar\OneDrive\Desktop\python-project\mega_01p%20jarvis\musicLibrary.py) - Music library configuration
- [client.py](file://c:\Users\Shashank%20Shekhar\OneDrive\Desktop\python-project\mega_01p%20jarvis\client.py) - Example Cohere AI client (reference)
- [requirements.txt](file://c:\Users\Shashank%20Shekhar\OneDrive\Desktop\python-project\mega_01p%20jarvis\requirements.txt) - Python dependencies

## Dependencies

- `speechrecognition` - Voice recognition
- `pyttsx3` - Text-to-speech engine
- `gtts` - Google Text-to-Speech
- `pygame` - Audio playback
- `requests` - HTTP requests
- `cohere` - Cohere AI API