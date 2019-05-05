from pykollib.request.GenericAdventuringRequest import GenericAdventuringRequest


class ChoiceRequest(GenericAdventuringRequest):
    "A request to choose an option for a choice adventure."

    def __init__(self, session, choiceId, choiceNumber):
        super(ChoiceRequest, self).__init__(session)
        self.url = session.server_url + "choice.php"
        self.requestData["pwd"] = session.pwd
        self.requestData["whichchoice"] = choiceId
        self.requestData["option"] = choiceNumber
