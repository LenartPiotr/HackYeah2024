from ollama import Client
from pathlib import Path

class Chat:
    def __init__(self):
        self.client = Client(host='http://localhost:11434')
        self.history = []
        self.lastQuestion = ''
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
                return 'To już wszystko. Upewnij się, że wszystkie dane zostały wprowadzone prawidłowo. Twój formularz jest gotowy do pobrania.'
            else:
                return self.ask_for_more_info(fields, message)
            
        # przykład: fields: {'A':["Kod urzędu skarbowego"], 'B':["Imię", "Nazwisko"], 'D':[]}
        return "Basinga!"
    
    # Zwraca tablice wszystkich wiadomości napisanych przez użytkownika do analizy do parsera
    def getHistory(self):
        return [x['content'] for x in self.history]
    
    # Niech wygeneruje tekst nie rozpoznania parsera - parser: str
    def undefinedParser(self, parser):
        return f'Wybrano formularz {parser}, który nie jest obecnie zaimplementowany.'
    
    # Ustawiony nowy parser - newParser to obiekt
    def switchParser(self, newParser):
        fields = newParser.get_what_needed()
        return self.ask_for_more_info(fields, 'Jakie informacje mam podać?')
    
    def inform_about_PCC(self, line):
        response = self.client.chat(model='llama3.2', messages=[
            {
                'role': 'system', 'content': self.pcc_system_prompt,
            }] + [
            {
                'role': 'user', 'content': line,
            },
        ])
        response = response['message']['content']
        self.history.append({
            'role': 'assistant', 'content': response
        })

        return response
    
    def ask_for_more_info(self, fields, message):
        highest_category = sorted(fields.keys())[0]
        missing_info = ', '.join(fields[highest_category])
        system = self.more_info_system_prompt.replace('<missing_info>', missing_info)
        messages = [
            {'role': 'system', 'content': system},
            {'role': 'assistant', 'content': self.lastQuestion},
            {'role': 'user', 'content': message}
        ]
        
        print(messages)
        response = self.client.chat(model='llama3.2', messages=messages)

        response = response['message']['content']
        self.history.append({
            'role': 'assistant', 'content': response
        })

        self.lastQuestion = response

        return response
