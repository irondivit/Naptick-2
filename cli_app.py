import os
from loader import build_rag_agent
from speech_utils import transcribe_audio, speak_text

def record_audio(filename="input.wav"):
    import sounddevice as sd
    import numpy as np
    from scipy.io.wavfile import write

    print("🎤 Recording for 8 seconds...")
    fs = 44100  # Sample rate
    seconds = 8

    # Record mono audio
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # Save in correct format
    write(filename, fs, recording)
    print(f"✅ Recorded audio saved as {filename}")
    return filename


def main():
    agent = build_rag_agent()

    print("🧠 Welcome to the Sleep Coach CLI!")
    while True:
        user_input_mode = input("\nPress [Enter] to talk or type 'exit' to quit: ")
        if user_input_mode.lower() == "exit":
            break

        # Step 1: Record and transcribe
        audio_path = record_audio()
        try:
            user_text = transcribe_audio(audio_path)
        except Exception as e:
            print("❌ Could not transcribe audio:", e)
            continue

        print(f"👤 You said: {user_text}")

        # Step 2: Get response from Gemini agent
        contextual_prompt = f"""
        You are a sleep coach trained on CSVs containing: Sleep Duration, Deep Sleep, Wake Episodes, Daily Steps, and Stress Levels.

        Compare the user’s stats with benchmark ranges and dataset trends if available.

        Always look for patterns across multiple users to answer general questions.

        Use this data to answer:

        User query: {user_text}
        """

        response = agent.invoke(contextual_prompt)

        # Step 3: Display and speak response
        print(f"🤖 Coach: {response['result']}")
        speak_text(response["result"])


if __name__ == "__main__":
    main()
