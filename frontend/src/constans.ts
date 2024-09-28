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
    name: {
        polish: 'Pierwsze imię',
        english: 'Name',
        ukrainian: "Ім'я"
    },
    surname: {
        polish: 'Nazwisko',
        english: 'Surname',
        ukrainian: 'Прізвище'
    },
    birthDate: {
        polish: 'Data urodzenia',
        english: 'Date of birth',
        ukrainian: 'Дата народження'
    },
    country: {
        polish: 'Kraj',
        english: 'Country',
        ukrainian: 'Країна'
    },
    subjectOfTax: {
        polish: 'Przedmiot opodatkowania',
        english: 'Tax subject',
        ukrainian: "Об'єкт оподаткування"
    },
    typeOfCivilLawActivity: {
        polish: 'Rodzaj czynności cywilnoprawnej',
        english: 'Type of civil law activity',
        ukrainian: 'Вид цивільно-правової діяльності'
    },
    typeOfCompany: {
        polish: 'Typ spółki',
        english: 'Type of company',
        ukrainian: 'Тип компанії'
    }
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