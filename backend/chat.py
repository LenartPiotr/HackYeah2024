from ollama import Client
from pathlib import Path

class Chat:
    def __init__(self):
        self.client = Client(host='http://localhost:11434')
        self.history = []
        with open(Path(__file__).parent / 'system_prompts' / 'inform_about_pcc.txt', encoding='utf-8') as f:
            self.pcc_system_prompt = f.read()
        with open(Path(__file__).parent / 'system_prompts' / 'ask_for_more_info.txt', encoding='utf-8') as f:
            self.more_info_system_prompt = f.read()

    # Message - wprowadzona wiadomość
    # Parser - wybrany parser dokumentu lub None
    def message(self, message, parser):
        self.history.append({'role': 'user', 'content': message})
        if parser is None:
            return self.inform_about_PCC(message)

        if parser is not None:
            fields = parser.get_what_needed()
            if fields == {}:
                return 'Basinga!'
            else:
                return self.ask_for_more_info(fields)
            
        # przykład: fields: {'A':["Kod urzędu skarbowego"], 'B':["Imię", "Nazwisko"], 'D':[]}
        return "Basinga!"
    
    # Zwraca tablice wszystkich wiadomości napisanych przez użytkownika do analizy do parsera
    def getHistory(self):
        return self.history
    
    # Niech wygeneruje tekst nie rozpoznania parsera - parser: str
    def undefinedParser(self, parser):
        return f'Wybrano formularz {parser}, który nie jest obecnie zaimplementowany.'
    
    # Ustawiony nowy parser - newParser to obiekt
    def switchParser(self, newParser):
        return 'Swing to new Parser!'
    
    def inform_about_PCC(self, line):
        response = self.client.chat(model='llama3.2', messages=[
            {
                'role': 'system', 'content': self.pcc_system_prompt,
            }] + self.history + [
            {
                'role': 'user', 'content': line,
            },
        ])
        response = response['message']['content']
        self.history.append({
            'role': 'assistant', 'content': response
        })

        return response
    
    def ask_for_more_info(self, fields):
        highest_category = sorted(fields.keys())[0]
        missing_info = ', '.join(fields[highest_category])
        system = self.more_info_system_prompt.replace('<missing_info', missing_info)
        response = self.client.chat(model='llama3.2', messages=[
            {'role': 'system', 'content': system}
        ] + self.history)

        response = response['message']['content']
        self.history.append({
            'role': 'assistant', 'content': response
        })

        return response
