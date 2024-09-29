from ollama import Client
client = Client(host='http://localhost:11434')

system = '''
Jesteś algorytmem do ekstrakcji danych. Twoim zadaniem jest przeanalizować wypowiedź użytkownika.
Jeżeli użytkownik poda swoje imię, nazwisko, adres lub inną wartość, zastąp x w odpowiednim miejscu informacją, którą podał. Jeżeli jego wiadomość nie zawiera potrzebnej informacji, zastąp x wyrażeniem "nie podano".
Daty podawaj w formacie RRRR-MM-DD.
Twoja odpowiedź powinna być skonstruowana w następujący sposób:
'''

# Pierwsze imię: x
# Nazwisko: x
# Pesel: x
# data urodzenia: x
# Imię ojca: x
# Imię matki: x
# województwo zamieszkania: x
# powiat zamieszkania: x
# gmina zamieszkania: x
# ulica lub osiedle zamieszkania: x
# nr domu zamieszkania: x
# nr lokalu zamieszkania: x
# miejscowość zamieszkania: x
# kod pocztowy zamieszkania: x
# Data dokonania czynności: x
# Ostateczna wartość pieniężna: x
# Opis przedmiotu w formie bezosobowej: x
# Nazwa urzędu skarbowego w mianowniku: x

def message(args, mess):
    s = system + args
    response = client.chat(model='llama3.2', messages=[
        {
            'role': 'system', 'content': s,
        },
        {
            'role': 'user', 'content': mess,
        },
    ])
    return response['message']['content']