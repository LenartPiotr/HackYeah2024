from parsers import *
from chat import Chat

class App:
    selectedParser = None
    
    def __init__(self):
        self.chat = Chat()
    
    def message(self, message):
        res = {
            'responses': [],
            'next_question': ''
        }
        if self.selectedParser is not None:
            res['responses'] = self.selectedParser.message(message)
        res['next_question'] = self.chat.message(message, self.selectedParser)
        return res
    
    def change_document(self, document):
        newParser = None
        if document == 'PCC-3':
            newParser = Parser_PCC3()
        # Add other parsers here
        if newParser is None:
            return {
                'responses': [],
                'next_question': self.chat.undefinedParser(document)
            }
        answer = self.chat.switchParser(newParser)
        allMessages = self.chat.getHistory()
        responses = newParser.message('\n'.join(allMessages))
        return {
            'responses': responses,
            'next_question': answer
        }
    
    def edit(self, category, key, value):
        if self.selectedParser is not None:
            self.selectedParser.update_value(category, key, value)
    
    def xml(self):
        if self.selectedParser is not None:
            return self.selectedParser.generate_xml()
        return ''
