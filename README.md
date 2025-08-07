# Voice_to_voice_translator_in_different_languages
##What This Code Does?
Records Audio Input via microphone using Gradio.

Transcribes Speech to English text using AssemblyAI.

Translates English text into Russian, Turkish, Japanese, and Hindi using the translate library.

Generates Speech for each translation using ElevenLabs text-to-speech API.

Returns Audio Outputs and transcribed text to the user via Gradio.

##Example Gradio UI Output
When you run this, you’ll see:

A microphone button

One transcribed text output

Four audio players (Russian, Turkish, Japanese, Hindi)

# 🎙️ Voice-to-Voice Translator

This is a simple Voice-to-Voice Translator web app built with **Gradio**, **AssemblyAI**, **Translate**, and **ElevenLabs**. It takes English audio input, transcribes it, translates the text into multiple languages, and converts each translation back into speech.

---

## 🌍 Features

- 🎤 **Record English Speech**
- ✍️ **Transcribe** speech to text using **AssemblyAI**
- 🌐 **Translate** the text into:
  - Russian 🇷🇺
  - Turkish 🇹🇷
  - Japanese 🇯🇵
  - Hindi 🇮🇳
- 🔊 **Convert translated text to speech** using **ElevenLabs**
- 🖥️ Easy-to-use web interface powered by **Gradio**

---

## 🧰 Requirements

Install dependencies with:

```bash
pip install gradio assemblyai translate elevenlabs


