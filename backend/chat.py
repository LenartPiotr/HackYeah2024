from ollama import Client
client = Client(host='http://localhost:11434')

class Chat:
    def __init__(self):
        self.history = []

    # Message - wprowadzona wiadomość
    # Parser - wybrany parser dokumentu lub None
    def message(self, message, parser):
        self.history.append(message)
        if parser is None:
            return self.inform_about_PCC(message)

        # if parser is not None:
        #   fields = parser.get_what_needed()
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
        system = '''
Twoim zadaniem jest rozpoznanie, czy pytanie zadane przez użytkownika dotyczy sytuacji, w której konieczne jest wypełnienie formularza podatkowego.
Formularz PCC-3 stosuje się wyłącznie w przypadku, gdy doszło do zakupu samochodu, na który obowiązuje podatek od czynności cywilnoprawnych.
Gdy użytkownik zapyta o sytuację, gdzie doszło do zakupu samochodu, na który obowiązuje podatek poinformuj go o konieczności wypełnienia formularza PCC-3.
Gdy użytkownik zapyta o jakąkolwiek inną sytuację, która nie odnosi się do zakupu samochodu oraz obowiązku zapłaty podatku od tej transakcji, powinieneś poinformować, że taki formularz nie jest obecnie obsługiwany.
Odpowiedź powinna być krótka i zwięzła przedstawiając tylko informacje czy należy wypełniać formularz PCC-3.
'''
        response = client.chat(model='llama3.2', messages=[
            {
                'role': 'system', 'content': system,
            },
            {
                'role': 'user', 'content': line,
            },
        ])

        return response['message']['content']