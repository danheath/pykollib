from enum import Enum

import pykollib

from ..util import parsing
from .clan_rumpus import Furniture
from .request import Request


class MeatFurniture(Enum):
    Orchid = Furniture.MeatOrchid
    Tree = Furniture.MeatTree
    Bush = Furniture.MeatBush


class clan_rumpus_meat(Request):
    """
    Uses a meat dispenser in the clan rumpus room.
    """
    def __init__(self, session: "pykollib.Session", furniture: MeatFurniture) -> None:
        super().__init__(session)
        spot, furni = furniture.value

        params = {"action": "click", "spot": spot, "furni": furni}
        self.request = session.request("clan_rumpus.php", params=params)

    @staticmethod
    async def parser(html: str, **kwargs) -> int:
        return parsing.meat(html)
