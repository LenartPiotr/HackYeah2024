import re
import xml.etree.ElementTree as ET
import datetime

class Parser_PCC3:
    def __init__(self):
        self.fields = {
            'A': {
                "transaction_date": "",
                "office_code": "",
            },
            'B': {
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
            },
            'D': {
                "final_value": "",
                "item_description": "",
            },
        }

    def parse_word(self, value: str):
        match = re.search(r"[a-ząćęłńóśżźA-ZĄĆĘŁŃÓŚŻŹ]+", value)
        return match.group(0) if match else None

    def parse_pesel(self, value: str):
        match = re.search(r"\d{11}", value)
        return match.group(0) if match else None

    def parse_date(self, value: str):
        match = re.search(
            r"(?P<forward>\d{2}-\d{2}-\d{4})|(?P<reverse>\d{4}-\d{2}-\d{2})|(?P<word>[a-ząćęłńóśżźA-ZĄĆĘŁŃÓŚŻŹ]+)",
            value,
        )
        if not match:
            return None
        if date := match.group("forward"):
            return f"{date[6:]}-{date[3:5]}-{date[0:2]}"
        if date := match.group("reverse"):
            return date
        if date := match.group("word").lower().replace(" ", ""):
            match date:
                case "wczoraj" | "yesterday":
                    return (datetime.date.today() - datetime.timedelta(1)).strftime(
                        "%Y-%m-%d"
                    )
                case "przedwczoraj" | "thedaybeforeyesterday" | "daybeforeyesterday":
                    return (datetime.date.today() - datetime.timedelta(2)).strftime(
                        "%Y-%m-%d"
                    )
        return None

    def parse_postal(self, value: str):
        match = re.search(r'\d{2}-\d{3}', value)
        return match.group(0) if match else None

    def parse_number(self, value: str):
        match = re.search(r'\d+', value)
        return match.group(0) if match else None

    def parse_money(self, value: str):
        match = re.search(r'.*?(\d+)', value)
        return match.group(1) if match else None

    def parse_sentence(self, value: str):
        return value.strip()

    def validate(self, value: str):
        return value

    def parse_message(self, message: str):
        patterns = {
            r"Pierwsze imię: ([^\n]+)": {
                "field": "first_name",
                'category': 'B',
                "parse": self.parse_word,
                "validate": self.validate
            },
            r"Nazwisko: ([^\n]+)": {"field": "last_name", 'category': 'B', "parse": self.parse_word, 'validate': self.validate},
            r"Pesel: ([^\n]+)": {"field": "pesel", 'category': 'B', "parse": self.parse_pesel, 'validate': self.validate},
            r"data urodzenia: ([^\n]+)": {
                "field": "birth_date",
                'category': 'B',
                "parse": self.parse_date,
                'validate': self.validate
            },
            r"Imię ojca: ([^\n]+)": {"field": "father_name", 'category': 'B', "parse": self.parse_word, 'validate': self.validate},
            r"Imię matki: ([^\n]+)": {"field": "mother_name", 'category': 'B', "parse": self.parse_word, 'validate': self.validate},
            r"województwo zamieszkania: ([^\n]+)": {
                "field": "province",
                'category': 'B',
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"powiat zamieszkania: ([^\n]+)": {
                "field": "district",
                'category': 'B',
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"gmina zamieszkania: ([^\n]+)": {
                "field": "municipality",
                'category': 'B',
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"ulica zamieszkania: ([^\n]+)": {
                "field": "street",
                'category': 'B',
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"osiedle zamieszkania: ([^\n]+)": {
                "field": "neighborhood",
                'category': 'B',
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"nr domu zamieszkania: ([^\n]+)": {
                "field": "house_number",
                'category': 'B',
                "parse": self.parse_number,
                'validate': self.validate
            },
            r"nr lokalu zamieszkania: ([^\n]+)": {
                "field": "apartment_number",
                'category': 'B',
                "parse": self.parse_number,
                'validate': self.validate
            },
            r"miejscowość zamieszkania: ([^\n]+)": {
                "field": "city",
                'category': 'B',
                "parse": self.parse_word,
                'validate': self.validate
            },
            r"kod pocztowy zamieszkania: ([^\n]+)": {
                "field": "postal_code",
                'category': 'B',
                "parse": self.parse_postal,
                'validate': self.validate
            },
            r"Data dokonania czynności: ([^\n]+)": {
                "field": "transaction_date",
                'category': 'A',
                "parse": self.parse_date,
                'validate': self.validate
            },
            r"Ostateczna wartość pieniężna: ([^\n]+)": {
                "field": "final_value",
                'category': 'D',
                "parse": self.parse_money,
                'validate': self.validate
            },
            r"Opis przedmiotu: ([^\n]+)": {
                "field": "item_description",
                'category': 'D',
                "parse": self.parse_sentence,
                'validate': self.validate
            },
        }

        for pattern, entry in patterns.items():
            match = re.search(pattern, message)
            try:
                if match and (value := match.group(1)) is not None:
                    field, parse, validate, category = (
                        entry["field"],
                        entry["parse"],
                        entry["validate"],
                        entry['category'],
                    )
                    try:
                        self.fields[category][field] = validate(parse(value))
                    except Exception:
                        pass
            except IndexError:
                pass

    def __str__(self):
        return (
            f"Pierwsze imię: {self.fields['B']['first_name']}\n"
            f"Nazwisko: {self.fields['B']['last_name']}\n"
            f"Pesel: {self.fields['B']['pesel']}\n"
            f"Data urodzenia: {self.fields['B']['birth_date']}\n"
            f"Imię ojca: {self.fields['B']['father_name']}\n"
            f"Imię matki: {self.fields['B']['mother_name']}\n"
            f"Województwo zamieszkania: {self.fields['B']['province']}\n"
            f"Powiat zamieszkania: {self.fields['B']['district']}\n"
            f"Gmina zamieszkania: {self.fields['B']['municipality']}\n"
            f"Ulica zamieszkania: {self.fields['B']['street']}\n"
            f"Osiedle zamieszkania: {self.fields['B']['neighborhood']}\n"
            f"Nr domu zamieszkania: {self.fields['B']['house_number']}\n"
            f"Nr lokalu zamieszkania: {self.fields['B']['apartment_number']}\n"
            f"Miejscowość zamieszkania: {self.fields['B']['city']}\n"
            f"Kod pocztowy zamieszkania: {self.fields['B']['postal_code']}\n"
            f"Data dokonania czynności: {self.fields['A']['transaction_date']}\n"
            f"Ostateczna wartość pieniężna: {self.fields['D']['final_value']}\n"
            f"Opis przedmiotu: {self.fields['D']['item_description']}"
        )

    def no_none(self, value, default='0'):
        return value if value is not None else default

    def generate_xml(self):
        # Tworzenie elementów XML
        deklaracja = ET.Element('Deklaracja', xmlns="http://crd.gov.pl/wzor/2023/12/13/13064/")

        # Nagłówek
        naglowek = ET.SubElement(deklaracja, 'Naglowek')
        kod_formularza = ET.SubElement(naglowek, 'KodFormularza', kodSystemowy="PCC-3 (6)", kodPodatku="PCC", rodzajZobowiazania="Z", wersjaSchemy="1-0E")
        kod_formularza.text = "PCC-3"
        wariant_formularza = ET.SubElement(naglowek, 'WariantFormularza')
        wariant_formularza.text = "6"
        cel_zlozenia = ET.SubElement(naglowek, 'CelZlozenia', poz="P_6")
        cel_zlozenia.text = "1"
        data = ET.SubElement(naglowek, 'Data', poz="P_4")
        data.text = self.no_none(self.fields['A']['transaction_date'])
        kod_urzedu = ET.SubElement(naglowek, 'KodUrzedu')
        kod_urzedu.text = "0271"

        # Podmiot1 (Podatnik)
        podmiot1 = ET.SubElement(deklaracja, 'Podmiot1', rola="Podatnik")
        osoba_fizyczna = ET.SubElement(podmiot1, 'OsobaFizyczna')
        pesel = ET.SubElement(osoba_fizyczna, 'PESEL')
        pesel.text = self.no_none(self.fields['B']['pesel'])
        imie_pierwsze = ET.SubElement(osoba_fizyczna, 'ImiePierwsze')
        imie_pierwsze.text = self.no_none(self.fields['B']['first_name'])
        nazwisko = ET.SubElement(osoba_fizyczna, 'Nazwisko')
        nazwisko.text = self.no_none(self.fields['B']['last_name'])
        data_urodzenia = ET.SubElement(osoba_fizyczna, 'DataUrodzenia')
        data_urodzenia.text = self.no_none(self.fields['B']['birth_date'])

        # Adres zamieszkania
        adres_zamieszkania = ET.SubElement(podmiot1, 'AdresZamieszkaniaSiedziby', rodzajAdresu="RAD")
        adres_pol = ET.SubElement(adres_zamieszkania, 'AdresPol')
        kod_kraju = ET.SubElement(adres_pol, 'KodKraju')
        kod_kraju.text = "PL"
        wojewodztwo = ET.SubElement(adres_pol, 'Wojewodztwo')
        wojewodztwo.text = self.no_none(self.fields['B']['province'])
        powiat = ET.SubElement(adres_pol, 'Powiat')
        powiat.text = self.no_none(self.fields['B']['district'])
        gmina = ET.SubElement(adres_pol, 'Gmina')
        gmina.text = self.no_none(self.fields['B']['municipality'])
        ulica = ET.SubElement(adres_pol, 'Ulica')
        ulica.text = self.no_none(self.fields['B']['street'])
        nr_domu = ET.SubElement(adres_pol, 'NrDomu')
        nr_domu.text = self.no_none(self.fields['B']['house_number'])
        nr_lokalu = ET.SubElement(adres_pol, 'NrLokalu')
        nr_lokalu.text = self.no_none(self.fields['B']['apartment_number'])
        miejscowosc = ET.SubElement(adres_pol, 'Miejscowosc')
        miejscowosc.text = self.no_none(self.fields['B']['city'])
        kod_pocztowy = ET.SubElement(adres_pol, 'KodPocztowy')
        kod_pocztowy.text = self.no_none(self.fields['B']['postal_code'])

        # Pozycje szczegółowe
        pozycje_szczegolowe = ET.SubElement(deklaracja, 'PozycjeSzczegolowe')
        p7 = ET.SubElement(pozycje_szczegolowe, 'P_7')
        p7.text = "2"
        # Przedmiot opodatkowania
        p20 = ET.SubElement(pozycje_szczegolowe, 'P_20')
        p20.text = "1"
        # Miejsce położenia rzeczy lub miejsce wykonywania prawa majątkowego
        p21 = ET.SubElement(pozycje_szczegolowe, 'P_21')
        p21.text = "1"
        # Miejsce dokonania czynności cywilnoprawnej
        p22 = ET.SubElement(pozycje_szczegolowe, 'P_22')
        p22.text = "1"
        # Zwięzłe określenie treści i przedmiotu czynności cywilnoprawnej
        p23 = ET.SubElement(pozycje_szczegolowe, 'P_23')
        p23.text = self.no_none(self.fields['D']['item_description'])

        # Podatki i wartości
        value_24 = int(self.no_none(self.fields['D']['final_value'], 0))
        tax_25 = round(value_24 * 0.01)
        value_26 = 0
        tax_27 = round(value_26 * 0.02)
        result_46 = tax_25 + tax_27
        result_53 = result_46

        p24 = ET.SubElement(pozycje_szczegolowe, 'P_24')
        p24.text = str(value_24)
        p25 = ET.SubElement(pozycje_szczegolowe, 'P_25')
        p25.text = str(tax_25)
        p26 = ET.SubElement(pozycje_szczegolowe, 'P_26')
        p26.text = str(value_26)
        p27 = ET.SubElement(pozycje_szczegolowe, 'P_27')
        p27.text = str(tax_27)
        p46 = ET.SubElement(pozycje_szczegolowe, 'P_46')
        p46.text = str(result_46)
        p53 = ET.SubElement(pozycje_szczegolowe, 'P_53')
        p53.text = str(result_53)
        p62 = ET.SubElement(pozycje_szczegolowe, 'P_62')
        p62.text = "1"

        # Pouczenia
        pouczenia = ET.SubElement(deklaracja, 'Pouczenia')
        pouczenia.text = "1"

        xml_str = ET.tostring(deklaracja, encoding="utf-8", method="xml")

        return xml_str

sample_message = """
Pierwsze imię: Jan
Nazwisko: Kowalski
Pesel: 54121832134
data urodzenia: 1954-12-18
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
Data dokonania czynności: 2024-07-29
Ostateczna wartość pieniężna: 5000
Opis przedmiotu: kupienie samochodu na giełdzie
"""

if __name__ == '__main__':
    parser = Parser_PCC3()
    parser.parse_message(sample_message)
    print(parser)
    print(parser.generate_xml())
