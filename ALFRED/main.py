from core.command_brain import CommandBrain
from voice.stt import SpeechToText
from voice.tts import TextToSpeech

def main():
    brain = CommandBrain()
    stt = SpeechToText()
    tts = TextToSpeech()

    print("---------------------------")
    print("  A.L.F.R.E.D.")
    print("  Artificial Logic Framework for Reasoning, Execution and Development")
    print("  Version : 1.0.0")
    print("  Author  : Jovi")
    print("--------------------------")

    while True:
        
        user_input = stt.listen()
        if not user_input:
            continue

        comando = user_input.strip()

        
        if not comando:
            tts.speak("Sim, senhor?")
            continue

        print("ALFRED:", end=" ", flush=True)

        
        for chunk in brain.process_stream(comando):
            print(chunk, end="", flush=True)
            tts.speak_stream(chunk)

        
        tts._flush_buffer()
        print()


if __name__ == "__main__":
    main()
