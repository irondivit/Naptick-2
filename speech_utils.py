import os
import platform
import speech_recognition as sr
from gtts import gTTS
import tempfile
from tempfile import NamedTemporaryFile
import uuid

# ✅ 1. Speech-to-Text
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        return recognizer.recognize_google(audio)

# ✅ 2. Text-to-Speech with immediate playback
def speak_text(text):
    tts = gTTS(text=text)

    # Generate a safe temp file path manually
    tmp_path = os.path.join(tempfile.gettempdir(), f"gtts_{uuid.uuid4().hex}.mp3")
    
    # Save the speech
    tts.save(tmp_path)

    # Play the speech
    if platform.system() == "Windows":
        import playsound
        playsound.playsound(tmp_path)
    else:
        os.system(f"afplay {tmp_path}" if platform.system() == "Darwin" else f"mpg123 {tmp_path}")

    # Clean up
    os.remove(tmp_path)