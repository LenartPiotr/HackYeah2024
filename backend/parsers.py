import re

class Parser_PCC3:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.pesel = None
        self.birth_date = None
        self.father_name = None
        self.mother_name = None
        self.province = None
        self.district = None
        self.municipality = None
        self.street = None
        self.neighborhood = None
        self.house_number = None
        self.apartment_number = None
        self.city = None
        self.postal_code = None
        self.transaction_date = None
        self.final_value = None
        self.item_description = None

    def parse_word(self, value):
        match = re.search(r'[\\w\\s ]+: ([a-zA-Z]+)')
        return match.group(1) if match else None
    def parse_pesel(self, value):
        match = re.search(r'[\\w\\s ]+: (\\d{11})')
        return match.group(1) if match else None
    def parse_date(self, value):
        match = re.search(r'')

    def parse_message(self, message):
        patterns = {
            'first_name': r'Pierwsze imię: ([^\n]+)',
            'last_name': r'Nazwisko: ([^\n]+)',
            'pesel': r'Pesel: ([^\n]+)',
            'birth_date': r'data urodzenia: ([^\n]+)',
            'father_name': r'Imię ojca: ([^\n]+)',
            'mother_name': r'Imię matki: ([^\n]+)',
            'province': r'województwo zamieszkania: ([^\n]+)',
            'district': r'powiat zamieszkania: ([^\n]+)',
            'municipality': r'gmina zamieszkania: ([^\n]+)',
            'street': r'ulica zamieszkania: ([^\n]+)',
            'neighborhood': r'osiedle zamieszkania: ([^\n]+)',
            'house_number': r'nr domu zamieszkania: ([^\n]+)',
            'apartment_number': r'nr lokalu zamieszkania: ([^\n]+)',
            'city': r'miejscowość zamieszkania: ([^\n]+)',
            'postal_code': r'kod pocztowy zamieszkania: ([^\n]+)',
            'transaction_date': r'Data dokonania czynności: ([^\n]+)',
            'final_value': r'Ostateczna wartość pieniężna: ([^\n]+)',
            'item_description': r'Opis przedmiotu: ([^\n]+)'
        }

        for field, pattern in patterns.items():
            match = re.search(pattern, message)
            if match:
                setattr(self, field, match.group(1))

    def __str__(self):
        return (f"Pierwsze imię: {self.first_name}\n"
                f"Nazwisko: {self.last_name}\n"
                f"Pesel: {self.pesel}\n"
                f"Data urodzenia: {self.birth_date}\n"
                f"Imię ojca: {self.father_name}\n"
                f"Imię matki: {self.mother_name}\n"
                f"Województwo zamieszkania: {self.province}\n"
                f"Powiat zamieszkania: {self.district}\n"
                f"Gmina zamieszkania: {self.municipality}\n"
                f"Ulica zamieszkania: {self.street}\n"
                f"Osiedle zamieszkania: {self.neighborhood}\n"
                f"Nr domu zamieszkania: {self.house_number}\n"
                f"Nr lokalu zamieszkania: {self.apartment_number}\n"
                f"Miejscowość zamieszkania: {self.city}\n"
                f"Kod pocztowy zamieszkania: {self.postal_code}\n"
                f"Data dokonania czynności: {self.transaction_date}\n"
                f"Ostateczna wartość pieniężna: {self.final_value}\n"
                f"Opis przedmiotu: {self.item_description}")

message = """
Pierwsze imię: Jan
Nazwisko: Kowalski
Pesel: 12345678901
data urodzenia: 1980-05-15
Imię ojca: Adam
Imię matki: Ewa
województwo zamieszkania: Mazowieckie
powiat zamieszkania: Warszawski
gmina zamieszkania: Śródmieście
ulica zamieszkania: Marszałkowska
osiedle zamieszkania: Centrum
nr domu zamieszkania: 15
nr lokalu zamieszkania: 12
miejscowość zamieszkania: Warszawa
kod pocztowy zamieszkania: 00-001
Data dokonania czynności: Wczoraj
Ostateczna wartość pieniężna: 5000
Opis przedmiotu: kupienie samochodu na giełdzie
"""

person = PersonInfo()
person.parse_message(message)
print(person)
