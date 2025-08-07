import gradio as gr
import assemblyai as aai
from translate import Translator
from elevenlabs import ElevenLabs, VoiceSettings
import uuid
from pathlib import Path
import os

# Set your API keys
ASSEMBLYAI_API_KEY = "your api assemblyai"
ELEVENLABS_API_KEY = "yours api 11lab"

def voice_to_voice(audio_file):
    try:
        # Transcribe the audio
        transcription_res = audio_transcription(audio_file)

        if transcription_res.status == aai.TranscriptStatus.error:
            raise gr.Error(f"Transcription error: {transcription_res.error}")
        
        text = transcription_res.text

        # Translate the transcribed text
        ru_translation, tr_translation, ja_translation, hi_translation = text_translation(text)

        # Convert translations to speech
        ru_audio_path = text_to_speech(ru_translation)
        tr_audio_path = text_to_speech(tr_translation)
        ja_audio_path = text_to_speech(ja_translation)
        hi_audio_path = text_to_speech(hi_translation)

        return text, ru_audio_path, tr_audio_path, ja_audio_path, hi_audio_path

    except Exception as e:
        raise gr.Error(f"An error occurred: {str(e)}")


def audio_transcription(audio_file):
    aai.settings.api_key = ASSEMBLYAI_API_KEY
    transcriber = aai.Transcriber()
    return transcriber.transcribe(audio_file)


def text_translation(text):
    # Using translate library
    translator_ru = Translator(from_lang="en", to_lang="ru")
    translator_tr = Translator(from_lang="en", to_lang="tr")
    translator_ja = Translator(from_lang="en", to_lang="ja")
    translator_hi = Translator(from_lang="en", to_lang="hi")


    ru_text = translator_ru.translate(text)
    tr_text = translator_tr.translate(text)
    ja_text = translator_ja.translate(text)
    hi_text = translator_hi.translate(text)

    return ru_text, tr_text, ja_text, hi_text


def text_to_speech(text):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam's voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.5,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

    save_file_path = f"{uuid.uuid4()}.mp3"
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: Audio file saved.")
    return save_file_path


# Gradio interface
audio_input = gr.Audio(sources=["microphone"], type="filepath")

demo = gr.Interface(
    fn=voice_to_voice,
    inputs=audio_input,
    outputs=[
        gr.Text(label="Transcribed Text"),
        gr.Audio(label="Russian"),
        gr.Audio(label="Turkish"),
        gr.Audio(label="Japanese"),
        gr.Audio(label="Hindi")
    ],
    title="Voice-to-Voice Translator",
    description="Speak English. Get translated audio in Russian, Turkish, Japanese, Hindi",
)

if __name__ == "__main__":
    demo.launch()