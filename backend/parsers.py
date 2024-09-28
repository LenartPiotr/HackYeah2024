import re
import xml.etree.ElementTree as ET

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
        data.text = self.no_none(self.transaction_date)
        kod_urzedu = ET.SubElement(naglowek, 'KodUrzedu')
        kod_urzedu.text = "0271"
        
        # Podmiot1 (Podatnik)
        podmiot1 = ET.SubElement(deklaracja, 'Podmiot1', rola="Podatnik")
        osoba_fizyczna = ET.SubElement(podmiot1, 'OsobaFizyczna')
        pesel = ET.SubElement(osoba_fizyczna, 'PESEL')
        pesel.text = self.no_none(self.pesel)
        imie_pierwsze = ET.SubElement(osoba_fizyczna, 'ImiePierwsze')
        imie_pierwsze.text = self.no_none(self.first_name)
        nazwisko = ET.SubElement(osoba_fizyczna, 'Nazwisko')
        nazwisko.text = self.no_none(self.last_name)
        data_urodzenia = ET.SubElement(osoba_fizyczna, 'DataUrodzenia')
        data_urodzenia.text = self.no_none(self.birth_date)
        
        # Adres zamieszkania
        adres_zamieszkania = ET.SubElement(podmiot1, 'AdresZamieszkaniaSiedziby', rodzajAdresu="RAD")
        adres_pol = ET.SubElement(adres_zamieszkania, 'AdresPol')
        kod_kraju = ET.SubElement(adres_pol, 'KodKraju')
        kod_kraju.text = "PL"
        wojewodztwo = ET.SubElement(adres_pol, 'Wojewodztwo')
        wojewodztwo.text = self.no_none(self.province)
        powiat = ET.SubElement(adres_pol, 'Powiat')
        powiat.text = self.no_none(self.district)
        gmina = ET.SubElement(adres_pol, 'Gmina')
        gmina.text = self.no_none(self.municipality)
        ulica = ET.SubElement(adres_pol, 'Ulica')
        ulica.text = self.no_none(self.street)
        nr_domu = ET.SubElement(adres_pol, 'NrDomu')
        nr_domu.text = self.no_none(self.house_number)
        nr_lokalu = ET.SubElement(adres_pol, 'NrLokalu')
        nr_lokalu.text = self.no_none(self.apartment_number)
        miejscowosc = ET.SubElement(adres_pol, 'Miejscowosc')
        miejscowosc.text = self.no_none(self.city)
        kod_pocztowy = ET.SubElement(adres_pol, 'KodPocztowy')
        kod_pocztowy.text = self.no_none(self.postal_code)

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
        p23.text = self.no_none(self.item_description)
        
        # Podatki i wartości
        value_24 = self.no_none(int(self.final_value), 0)
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
                f"Nr domu zamieszkania: {self.house_number}\n"
                f"Nr lokalu zamieszkania: {self.apartment_number}\n"
                f"Miejscowość zamieszkania: {self.city}\n"
                f"Kod pocztowy zamieszkania: {self.postal_code}\n"
                f"Data dokonania czynności: {self.transaction_date}\n"
                f"Ostateczna wartość pieniężna: {self.final_value}\n"
                f"Opis przedmiotu: {self.item_description}")

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
    parser.generate_xml('deklaracja.xml')
