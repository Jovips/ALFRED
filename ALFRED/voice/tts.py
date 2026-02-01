import pyttsx3
import re

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 140)
        self.engine.setProperty("volume", 1.0)
        self.is_speaking = False

        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[0].id)

        self.buffer = ""

    
    def speak(self, text: str):
        if not text.strip():
            return

        self.is_speaking = True
        print("ALFRED está falando...")
        self.engine.say(text)
        self.engine.runAndWait()
        print("ALFRED terminou de falar")
        self.is_speaking = False

    
    def speak_stream(self, chunk: str):
        self.buffer += chunk

        
        if re.search(r"[.!?]\s*$", self.buffer):
            self._flush_buffer()

    def _flush_buffer(self):
        text = self.buffer.strip()
        self.buffer = ""

        if not text:
            return

        self.is_speaking = True
        self.engine.say(text)
        self.engine.runAndWait()
        self.is_speaking = False
