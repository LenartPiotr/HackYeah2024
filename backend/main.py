from fastapi import FastAPI, Response
from parsers import Parser_PCC3, sample_message

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
    return {
        'responses': [
            { 'type': 'name', 'value': 'Jan', 'category': 'B' },
            { 'type': 'surname', 'value': 'Kowalski', 'category': 'B' }
        ],
        'next_question': 'Bazinga!'
    }

@app.get("/xml", response_class=Response)
def get_xml():
    parser = Parser_PCC3()
    parser.parse_message(sample_message)
    xml_str = parser.generate_xml()
    return Response(content=xml_str, media_type="application/xml")