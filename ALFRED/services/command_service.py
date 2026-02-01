import webbrowser
import os
import subprocess

class CommandService:
    def __init__(self):
        self.commands = {
            "open_browser": {
                "keywords": ["abre navegador", "abrir navegador", "open browser"],
                "action": self.open_browser
            },
            "open_explorer": {
                "keywords": ["abre explorador", "abrir pastas", "explorador"],
                "action": self.open_explorer
            },
            "open_vscode": {
                "keywords": ["abre vscode", "abrir código", "visual studio"],
                "action": self.open_vscode
            }
        }

    def execute(self, text: str):
        text = text.lower()

        for command in self.commands.values():
            for keyword in command["keywords"]:
                if keyword in text:
                    return command["action"]()

        return None

    def open_browser(self):
        webbrowser.open("https://google.com")
        return "Navegador aberto."

    def open_explorer(self):
        os.startfile("C:\\")
        return "Explorador de arquivos aberto."

    def open_vscode(self):
        subprocess.Popen(["code"])
        return "VS Code aberto."
