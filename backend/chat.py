class Chat:
    def __init__(self):
        pass
    # Message - wprowadzona wiadomość
    # Parser - wybrany parser dokumentu lub None
    def message(self, message, parser):

        # if parser is not None:
        #   fields = parser.get_what_needed()
        # przykład: fields: {'A':["Kod urzędu skarbowego"], 'B':["Imię", "Nazwisko"], 'D':[]}
        return "Basinga!"
    
    # Zwraca tablice wszystkich wiadomości napisanych przez użytkownika do analizy do parsera
    def getHistory(self):
        return []
    
    # Niech wygeneruje tekst nie rozpoznania parsera - parser: str
    def undefinedParser(self, parser):
        return 'Basigna nie rozpoznaje: ' + parser
    
    # Ustawiony nowy parser - newParser to obiekt
    def switchParser(self, newParser):
        return 'Swing to new Parser!'