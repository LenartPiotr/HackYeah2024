from fastapi import FastAPI, Response
from parsers import Parser_PCC3, sample_message

app = FastAPI()

@app.get("/")
def get():
    return {"ok": True}

@app.post("/message")
def message(response: str):
    return {
        'responses': [
            { 'type': 'Imię', 'value': 'Grzegorz', 'category': 'A' },
            { 'type': 'Nazwisko', 'value': 'Brzęczyszczykiewicz', 'category': 'A' }
        ],
        'next_question': 'Bazinga!'
    }

@app.get("/xml", response_class=Response)
def get_xml():
    parser = Parser_PCC3()
    parser.parse_message(sample_message)
    xml_str = parser.generate_xml()
    return Response(content=xml_str, media_type="application/xml")