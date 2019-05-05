from .GenericRequest import GenericRequest
from pykollib.util import ParseResponseUtils


class LookingGlassRequest(GenericRequest):
    "Uses the Looking Glass in the clan VIP room."

    def __init__(self, session):
        super(LookingGlassRequest, self).__init__(session)
        self.url = session.server_url + "clan_viplounge.php"
        self.requestData["action"] = "lookingglass"

    def parseResponse(self):
        self.responseData["items"] = ParseResponseUtils.parseItemsReceived(
            self.responseText, self.session
        )
