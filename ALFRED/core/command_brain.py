from services.command_service import CommandService
from core.brain import Brain

class CommandBrain(Brain):
    def __init__(self):
        super().__init__()
        self.command_service = CommandService()

    def process(self, user_input: str) -> str:
        intent = self.classify_intent(user_input)

        if intent == "command":
            result = self.command_service.execute(user_input)

            if result:
                return result
            else:
                return "Não entendi esse comando."

       
        return super().process(user_input)

    def classify_intent(self, text: str) -> str:
        intent = self.llm.classify_intent(text)

        if intent not in ["command", "chat"]:
            return "chat"

        return intent
    def process_stream(self, user_input: str):
        return super().process_stream(user_input)

