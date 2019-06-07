from typing import List, Union

import pykollib

from ..Error import (
    ItemNotFoundError,
    UnknownError,
    UserInHardcoreRoninError,
    UserIsIgnoringError,
    UserNotFoundError,
)
from ..types import ItemQuantity
from .request import Request


class kmail_send(Request):
    def __init__(
        self,
        session: "pykollib.Session",
        recipient: Union[int, str],
        message: str = "",
        items: List[ItemQuantity] = [],
        meat: int = 0,
    ) -> None:
        params = {"toid": ""}
        data = {
            "action": "send",
            "towho": recipient,
            "message": message,
            "sendmeat": meat,
        }

        self.request = session.request(
            "sendmessage.php", params=params, data=data, pwdt=True
        )

    @staticmethod
    async def parser(html: str, **kwargs) -> bool:
        if "<td>Invalid PlayerID.</td>" in html:
            raise UserNotFoundError("Invalid player ID.")

        if (
            "<center><table><tr><td>That player cannot receive Meat or items from other players right now."
            in html
        ):
            raise UserInHardcoreRoninError(
                "Unable to send items or meat. User is in hardcore or ronin."
            )

        if (
            "<center><table><tr><td>This message could not be sent, because you are on that player's ignore list.</td></tr></table></center>"
            in html
        ):
            raise UserIsIgnoringError("Unable to send message. User is ignoring us.")

        if (
            "<center><table><tr><td>You don't have enough of one of the items you're trying to send.</td></tr></table></center>"
            in html
        ):
            raise ItemNotFoundError(
                "You don't have enough of one of the items you're trying to send."
            )

        if (
            "<center><table><tr><td>That player would never use something as old and outmoded as"
            in html
        ):
            raise UserInHardcoreRoninError(
                "Unable to send items or meat. User is too trendy."
            )

        if (
            "<td>This message could not be sent, because that player is on your ignore list\.<\/td>"
            in html
        ):
            raise UserIsIgnoringError(
                "Unable to send message. We are ignoring the other player."
            )

        if "<td><center>Message sent.</center></td>" not in html:
            raise UnknownError("UnknownError")

        return True
