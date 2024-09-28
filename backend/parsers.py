import re
import datetime

class Parser_PCC3:
    def __init__(self):
        self.fields = {
            "first_name": "",
            "last_name": "",
            "pesel": "",
            "birth_date": "",
            "father_name": "",
            "mother_name": "",
            "province": "",
            "district": "",
            "municipality": "",
            "street": "",
            "neighborhood": "",
            "house_number": "",
            "apartment_number": "",
            "city": "",
            "postal_code": "",
            "transaction_date": "",
            "final_value": "",
            "item_description": "",
        }

    def parse_word(self, value: str):
        match = re.search(r"[a-ząćęłńóśżźA-ZĄĆĘŁŃÓŚŻŹ]+", value)
        return match.group(0) if match else None

    def parse_pesel(self, value: str):
        match = re.search(r"\\d{11}", value)
        return match.group(0) if match else None

    def parse_date(self, value: str):
        match = re.search(
            r"(?P<forward>\\d{2}-\\d{2}-\\d{4}})|(?P<reverse>\\d{4}-\\d{2}-\\d{2})|(?P<word>[a-ząćęłńóśżźA-ZĄĆĘŁŃÓŚŻŹ]+|(?:the *)?day *before *yester *day)",
            value,
        )
        if not match:
            return None
        try:
            date = match.group("forward")
            return f"{date[0:2]}-{date[3:5]}-{date[6:]}"
        except IndexError:
            pass
        try:
            return match.group("reverse")
        except IndexError:
            pass
        try:
            date = match.group("word").lower().replace(" ", "")

            match date:
                case "wczoraj" | "yesterday":
                    return (datetime.date.today() - datetime.timedelta(1)).strftime(
                        "%Y-%m-%d"
                    )
                case "przedwczoraj" | "thedaybeforeyesterday" | "daybeforeyesterday":
                    return (datetime.date.today() - datetime.timedelta(2)).strftime(
                        "%Y-%m-%d"
                    )

        except IndexError:
            pass
        return None

    def parse_postal(self, value: str):
        match = re.search(r'\\d{2}-\\d{3}', value)
        return match.group(0) if match else None

    def parse_number(self, value: str):
        match = re.search(r'\\d+', value)
        return match.group(0) if match else None

    def parse_money(self, value: str):
        match = re.search(r'.*?(\\d+)', value)
        return match.group(1) if match else None

    def parse_sentence(self, value: str):
        return value.strip()

    def validate(self, value: str):
        return value

    def parse_message(self, message: str):
        patterns = {
            r"Pierwsze imię: ([^\n]+)": {
                "field": "first_name",
                "parse": self.parse_word,
                "validate": self.validate
            },
            r"Nazwisko: ([^\n]+)": {"field": "last_name", "parse": self.parse_word, 'validate': self.validate},
            r"Pesel: ([^\n]+)": {"field": "pesel", "parse": self.parse_pesel, 'validate': self.validate},
            r"data urodzenia: ([^\n]+)": {
                "field": "birth_date",
                "parse": self.parse_date,
                'validate': self.validate
            },
            r"Imię ojca: ([^\n]+)": {"field": "father_name", "parse": self.parse_word, 'validate': self.validate},
            r"Imię matki: ([^\n]+)": {"field": "mother_name", "parse": self.parse_word, 'validate': self.validate},
            r"województwo zamieszkania: ([^\n]+)": {
                "field": "province",
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"powiat zamieszkania: ([^\n]+)": {
                "field": "district",
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"gmina zamieszkania: ([^\n]+)": {
                "field": "municipality",
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"ulica zamieszkania: ([^\n]+)": {
                "field": "street",
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"osiedle zamieszkania: ([^\n]+)": {
                "field": "neighborhood",
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"nr domu zamieszkania: ([^\n]+)": {
                "field": "house_number",
                "parse": self.parse_number,
                'validate': self.validate
            },
            r"nr lokalu zamieszkania: ([^\n]+)": {
                "field": "apartment_number",
                "parse": self.parse_number,
                'validate': self.validate
            },
            r"miejscowość zamieszkania: ([^\n]+)": {
                "field": "city",
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"kod pocztowy zamieszkania: ([^\n]+)": {
                "field": "postal_code",
                "parse": self.parse_postal,
                'validate': self.validate
            },
            r"Data dokonania czynności: ([^\n]+)": {
                "field": "transaction_date",
                "parse": self.parse_date,
                'validate': self.validate
            },
            r"Ostateczna wartość pieniężna: ([^\n]+)": {
                "field": "final_value",
                "parse": self.parse_money,
                'validate': self.validate
            },
            r"Opis przedmiotu: ([^\n]+)": {
                "field": "item_description",
                "parse": self.parse_sentence,
                'validate': self.validate
            },
        }

        for pattern, entry in patterns.items():
            match = re.search(pattern, message)
            try:
                if match and (value := match.group(1)) is not None:
                    field, parse, validate = (
                        entry["field"],
                        entry["parse"],
                        entry["validate"],
                    )
                    try:
                        self.fields[field] = validate(parse(value))
                    except Exception:
                        pass
            except IndexError:
                pass

    def __str__(self):
        return (
            f"Pierwsze imię: {self.fields['first_name']}\n"
            f"Nazwisko: {self.fields['last_name']}\n"
            f"Pesel: {self.fields['pesel']}\n"
            f"Data urodzenia: {self.fields['birth_date']}\n"
            f"Imię ojca: {self.fields['father_name']}\n"
            f"Imię matki: {self.fields['mother_name']}\n"
            f"Województwo zamieszkania: {self.fields['province']}\n"
            f"Powiat zamieszkania: {self.fields['district']}\n"
            f"Gmina zamieszkania: {self.fields['municipality']}\n"
            f"Ulica zamieszkania: {self.fields['street']}\n"
            f"Osiedle zamieszkania: {self.fields['neighborhood']}\n"
            f"Nr domu zamieszkania: {self.fields['house_number']}\n"
            f"Nr lokalu zamieszkania: {self.fields['apartment_number']}\n"
            f"Miejscowość zamieszkania: {self.fields['city']}\n"
            f"Kod pocztowy zamieszkania: {self.fields['postal_code']}\n"
            f"Data dokonania czynności: {self.fields['transaction_date']}\n"
            f"Ostateczna wartość pieniężna: {self.fields['final_value']}\n"
            f"Opis przedmiotu: {self.fields['item_description']}"
        )


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
