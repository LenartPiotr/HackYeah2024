from fastapi import FastAPI, Response
from app import App

from fastapi.middleware.cors import CORSMiddleware

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
    mainApp.change_document(document)

@app.get("/xml", response_class=Response)
def get_xml():
    return mainApp.xml()
    # parser = Parser_PCC3()
    # parser.parse_message(sample_message)
    # xml_str = parser.generate_xml()
    # return Response(content=xml_str, media_type="application/xml")

@app.post('/edit')
def edit(type):
    return {
        'responses': [],
        'next_question': 'Podaj wartość dla edytowalnego pola'
    }