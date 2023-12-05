from typing import Generator
from . import ernie

class FastErnie:
    def __init__(self, BAIDUID: str, BDUSS_BFESS: str):
        self.ernie = ernie.Ernie(BAIDUID, BDUSS_BFESS)
        self.sessionId = ''
        self.sessionName = ''
        self.parentChatId = '0'

    def askStream(self, question: str) -> Generator:
        if not self.sessionId:
            self.sessionName = question
        for data in self.ernie.askStream(question, self.sessionId, self.sessionName, self.parentChatId):
            yield data
        self.sessionId = data['sessionId']
        self.parentChatId = data['botChatId']
    
    def ask(self, question: str) -> dict:
        result = {}
        for data in self.askStream(question):
            result = data
        del result['done']
        return result
    
    def close(self) -> bool:
        if self.ernie.deleteConversation(self.sessionId):
            self.sessionId = ''
            self.sessionName = ''
            self.parentChatId = '0'
            return True
        return False