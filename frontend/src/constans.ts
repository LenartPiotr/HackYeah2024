// export const typeMap = {
//     name: 'Pierwsze imię',
//     surname: 'Nazwisko',
//     birthDate: 'Data urodzenia',
//     country: 'Kraj',
//     subjectOfTax: 'Przedmiot opodatkowania',
//     typeOfCivilLawActivity: 'Rodzaj czynności cywilnoprawnej',
//     typeOfCompany: 'Typ spółki',
// };
// export const typeMap = {
//     polish: {
//         name: 'Pierwsze imię',
//         surname: 'Nazwisko',
//         birthDate: 'Data urodzenia',
//         country: 'Kraj',
//         subjectOfTax: 'Przedmiot opodatkowania',
//         typeOfCivilLawActivity: 'Rodzaj czynności cywilnoprawnej',
//         typeOfCompany: 'Typ spółki',
//     },
//     english: {
//         name: 'Name',
//         surname: 'Surname',
//         birthDate: 'Date of birth',
//         country: 'Country',
//         subjectOfTax: 'Tax subject',
//         typeOfCivilLawActivity: 'Type of civil law activity',
//         typeOfCompany: 'Type of company',
//     },
//     ukrainian: {
//         name: "ім'я",
//         surname: 'прізвище',
//         birthDate: 'Дата народження',
//         country: 'країна',
//         subjectOfTax: "Об'єкт оподаткування",
//         typeOfCivilLawActivity: 'Вид цивільно-правової діяльності',
//         typeOfCompany: 'Тип компанії',
//     },
// };
export const typeMap = {
    first_name: {
        polish: 'Pierwsze imię',
        english: 'Name',
        ukrainian: "Ім'я"
    },
    last_name: {
        polish: 'Nazwisko',
        english: 'Surname',
        ukrainian: 'Прізвище'
    },
    birth_date: {
        polish: 'Data urodzenia',
        english: 'Date of birth',
        ukrainian: 'Дата народження'
    },
    pesel: {
        polish: 'PESEL',
        english: 'PESEL',
        ukrainian: 'PESEL'
    },
    father_name: {
        polish: 'Imię ojca',
        english: 'Father name',
        ukrainian: "Ім'я по батькові"
    },
    mother_name: {
        polish: 'Imię matki',
        english: 'Mother name',
        ukrainian: "Ім'я матері"
    },
    province: {
        polish: 'Województwo',
        english: 'Voivodeship',
        ukrainian: "Воєводство"
    },
    district: {
        polish: 'Powiat',
        english: 'County',
        ukrainian: "графство"
    },
    municipality: {
        polish: 'Gmina',
        english: 'Commune',
        ukrainian: "Комуна"
    },
    street: {
        polish: 'Ulica',
        english: 'Street',
        ukrainian: "вул"
    },
    house_number: {
        polish: 'Numer domu',
        english: 'House number',
        ukrainian: "Номер будинку"
    },
    apartment_number: {
        polish: 'Numer mieszkania',
        english: 'Apartment number',
        ukrainian: "Номер квартири"
    },
    city: {
        polish: 'Miejscowość',
        english: 'City',
        ukrainian: "Місто"
    },
    postal_code: {
        polish: 'Kod pocztowy',
        english: 'Postal code',
        ukrainian: "Поштовий індекс"
    },
    transaction_date: {
        polish: 'Data dokonania czynności',
        english: 'Date of the action',
        ukrainian: "Дата проведення акції"
    },
    office_code: {
        polish: 'Nazwa urzędu skarbowego',
        english: 'Name of the tax office',
        ukrainian: "Назва податкової служби"
    },
    final_value: {
        polish: 'Wartość pieniężna',
        english: 'Monetary value',
        ukrainian: "Договір купівлі-продажу"
    },
    item_description: {
        polish: 'Opis przedmiotu',
        english: 'Item description',
        ukrainian: "Грошова вартість"
    },
};

// export const categoryMap = {
//     B: 'B. Dane podatnika dokonującego zapłaty lub zwolnionego z podatku na podstawie art. 9 pkt 10 lit. B ustawy',
//     C: 'C. Przedmiot opodatkowania i treść czynności cywilnoprawnej',
//     D: 'D. Obliczenie należnego podatku od czynności cywilnoprawnych, z wyjątkiem umowy spółki lub jej zmiany',
//     E: 'E. Obliczenie należnego podatku od umowy spółki / zmiany umowy spółki',
//     F: 'F. Podatek do zapłaty',
//     G: 'G. Informacje dodatkowe',
//     instructions: 'Pouczenia',
//     summary: 'Podsumowanie'
// };
export const categoryMap = {
    A: {
        polish: 'Okres, miejsce i cel składania deklaracji',
        english: 'Period, place and purpose of submitting declarations',
        ukrainian: 'Період, місце та мета подання декларації'
    },
    B: {
        polish: 'B. Dane podatnika dokonującego zapłaty lub zwolnionego z podatku na podstawie art. 9 pkt 10 lit. B ustawy',
        english: 'B. Data of the taxpayer making payment or exempted from tax under Article 9(10)(B) of the Act',
        ukrainian: 'B. Інформація про оподатковувану особу, яка здійснює платіж або звільняється від сплати податку відповідно до розділу 9(10)(B) Закону'
    },
    C: {
        polish: 'C. Przedmiot opodatkowania i treść czynności cywilnoprawnej',
        english: 'C. Object of taxation and content of civil law activity',
        ukrainian: "C. Об'єкт оподаткування та зміст цивільно-правової угоди"
    },
    D: {
        polish: 'D. Obliczenie należnego podatku od czynności cywilnoprawnych, z wyjątkiem umowy spółki lub jej zmiany',
        english: 'D. Calculation of the tax due on civil law transactions, except for the partnership agreement or its amendment',
        ukrainian: 'D. Розрахунок податку з цивільно-правових правочинів, крім установчого договору або змін до нього'
    },
    E: {
        polish: 'E. Obliczenie należnego podatku od umowy spółki / zmiany umowy spółki',
        english: 'E. Calculation of the tax due on the memorandum of association / amendment to the memorandum of association',
        ukrainian: 'E. Розрахунок податку на реєстрацію статуту/змін до статуту'
    },
    F: {
        polish: 'F. Podatek do zapłaty',
        english: 'F. Tax to be paid',
        ukrainian: 'F. Податок до сплати'
    },
    G: {
        polish: 'G. Informacje dodatkowe',
        english: 'G. Additional Information',
        ukrainian: 'G. Додаткова інформація'
    },
    instructions: {
        polish: 'Pouczenia',
        english: 'Advisories',
        ukrainian: 'Поради'
    },
    summary: {
        polish: 'Podsumowanie',
        english: "Summary",
        ukrainian: 'Підсумок'
    }
};