import ollama

class LLMService:
    def __init__(self, model="mistral"):
        self.model = model

    def chat(self, messages, 
             temperature=0.3):
        response = ollama.chat(
            model=self.model,
            messages=messages,
            options={
                "temperature": temperature
            }
        )
        return response["message"]["content"]

    def generate_response(self, prompt, context):
        messages = context + [
            {"role": "user", "content": prompt}
        ]
        return self.chat(messages)

    def classify_intent(self, text: str) -> str:
        messages = [
            {
                "role": "system",
                "content": (
                    "Classifique a intenção da frase abaixo. "
                    "Responda apenas com: command ou chat."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ]

        response = self.chat(messages, temperature=0.0)
        return response.strip().lower()
    
    def generate_response_stream(self, prompt, context):
        messages = context + [{"role": "user", "content": prompt}]

        stream = ollama.chat(
            model=self.model,
            messages=messages,
            stream=True
        )

        for chunk in stream:
            if "message" in chunk and "content" in chunk["message"]:
                yield chunk["message"]["content"]
