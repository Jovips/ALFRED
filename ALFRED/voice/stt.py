import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self) -> str:
        with self.microphone as source:
            print(" | Ouvindo... |")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="pt-BR")
            print("Você:", text)
            return text

        except sr.UnknownValueError:
            return ""

        except sr.RequestError:
            print("Erro ao acessar o serviço de reconhecimento.")
            return ""


class VoiceService:
    def __init__(self):
        self.stt = SpeechToText()

    def get_user_input(self) -> str:
        return self.stt.listen()
