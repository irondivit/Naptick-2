
# 🧠 Naptick AI Challenge – Task 2  
**Voice-to-Voice Sleep Coaching Agent with Context-Aware Gemini Responses**

This project implements a voice-first, intelligent sleep coaching assistant using Google Gemini 1.5 Flash and LangChain. It processes user voice queries, transcribes them, retrieves relevant information from health, sleep, and wearable datasets using a Chroma-based RAG system, and generates spoken personalized responses via TTS.

---

## 🎯 Task Description

**Objective:**  
Build a voice-to-voice intelligent agent that understands user queries related to sleep health and delivers expert, context-aware coaching responses using domain data and Gemini's reasoning capabilities.

### ✅ Required Capabilities:
- Voice input and output (TTS and STT)
- Sleep domain adaptation via multi-dataset RAG
- Gemini-powered answers using LangChain
- Chroma vector store for retrieval
- CLI-based interface (speech-to-speech)

---

## 🧩 Datasets Used

- `Sleep_health_and_lifestyle_dataset.csv`: Lifestyle, sleep hours, stress, disorders
- `Sleep_Efficiency.csv`: Time in bed, total sleep, sleep efficiency
- `mental_health_wearable_data.csv`: Heart rate, sleep, steps, mood, mental health risk

These datasets are embedded as documents and queried during interaction.

---

## 🔧 Features Implemented

### 🎤 Voice Interaction
- Records 5-second audio snippets using `sounddevice`
- Uses Google Speech Recognition (STT) to transcribe audio
- Replies vocally using `gTTS` and `simpleaudio` (cross-platform playback)

### 📁 Multi-Dataset RAG
- CSV rows converted to `LangChain Documents`
- Embedded using `GoogleGenerativeAIEmbeddings`
- Indexed into `Chroma` vector store
- Queried using LangChain's `RetrievalQA` chain

### 🤖 Gemini LLM Integration
- Uses `gemini-1.5-flash` for factual, helpful answers
- Query is prepended with health-aware prompt
- Retrieval grounding improves accuracy

---

## 🗂 Project Structure

```
naptik2/
├── data/
│   ├── Sleep_health_and_lifestyle_dataset.csv
│   ├── Sleep_Efficiency.csv
│   └── mental_health_wearable_data.csv
│
├── rag_agent.py         # Builds the RAG pipeline
├── cli_app.py           # CLI voice interface
├── speech_utils.py      # STT + TTS support
├── requirements.txt
└── README.md
```

---

## ⚙️ Technology Stack

| Component         | Tool                         |
|-------------------|------------------------------|
| LLM               | Google Gemini 1.5 Flash      |
| Framework         | LangChain                    |
| Embeddings        | Google Generative Embeddings |
| Vector Store      | Chroma                       |
| STT               | Google SpeechRecognition     |
| TTS               | gTTS + simpleaudio           |
| Voice Recording   | sounddevice                  |
| CLI Interface     | Python CLI                   |
| Data Format       | CSV                          |

---

## 🛠 Setup Instructions

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Add your Gemini API key in `.env`:**

```env
GOOGLE_API_KEY=your_gemini_key_here
```

3. **Run the CLI:**

```bash
python cli_app.py
```

Then follow the CLI prompts to speak to your sleep coach.

---

## 💡 Example Prompts

- "Why do I wake up tired even after 8 hours of sleep?"
- "How can I improve my REM sleep based on my wearable data?"
- "What does my high heart rate and low sleep duration mean?"
- "Give me a routine to reduce my stress and improve deep sleep."

---

## 📚 Output Demonstration

- Real-time voice transcription
- Gemini-generated, dataset-informed sleep advice
- Voice playback of responses

