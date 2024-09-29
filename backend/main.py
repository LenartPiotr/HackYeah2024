from fastapi import FastAPI, Response
from app import App

from fastapi.middleware.cors import CORSMiddleware

test_messages = ['Kupno samochodu wiąże się z potrzebą odprowadzenia podatku IPCC-3. Kliknij w tę nazwę, aby rozpocząć wypełnianie formularza.',
                 'Doskonale! Zacznijmy od podstaw. Widzę, że podałeś już swoje imię i nazwisko oraz koszt samochodu, potrzebuję więc teraz twojego PESELu, adresu oraz nazwy twojego urzędu skarbowego.',
                 'Teraz jeszcze tylko kod pocztowy i mamy to z głowy.',
                 'Twój formularz jest gotowy do wysłania. Upewnij się jednak, że wszystkie pola zostały wypełnione prawidłowo. Nawet mnie zdarza się czasem pomylić']

test_messages_index = -1

test_answers = [[], [
    {'type': 'name', 'value': 'Jan', 'category': 'B'},
    {'type': 'surname', 'value': 'Kowalski', 'category': 'B'},
    {'type': 'final_value', 'value': '3000', 'category': 'D'},
], [
    {'type': 'pesel', 'value': '99091728838', 'category': 'B'},
    {'type': 'birth_date', 'value': '1999-09-17', 'category': 'B'},
]]


app = FastAPI()

mainApp = App()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get():
    return {"ok": True}

@app.post("/message")
def message(response):
    test_messages_index += 1
    return {
        'responses': test_answers[test_messages_index],
        'next_question': test_messages[test_messages_index]
    }
    return mainApp.message(response)
    # return {
    #     'responses': [
    #         { 'type': 'name', 'value': 'Jan', 'category': 'B' },
    #         { 'type': 'surname', 'value': 'Kowalski', 'category': 'B' }
    #     ],
    #     'next_question': 'Bazinga!'
    # }

@app.post('/select_document')
def select_document(document):
    return mainApp.change_document(document)

@app.get("/xml", response_class=Response)
def get_xml():
    return mainApp.xml()
    # parser = Parser_PCC3()
    # parser.parse_message(sample_message)
    # xml_str = parser.generate_xml()
    # return Response(content=xml_str, media_type="application/xml")

@app.post('/edit')
def edit(category, type, value):
    return mainApp.edit(category, type, value)