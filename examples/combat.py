"""
This file shows how you can use adventure using libkol
"""

import os
from dotenv import load_dotenv
from libkol import run, Session
from libkol.request.combat import CombatRound

load_dotenv()


async def do_combat(combat, start: CombatRound):
    monster_hp = await start.monster.get_hp()
    round = start

    while monster_hp > 0:
        round = await combat.attack()
        monster_hp -= round.damage

    return round


async def main():
    async with Session() as kol:
        await kol.login(os.getenv("KOL_USERNAME"), os.getenv("KOL_PASSWORD"))
        result = await kol.adventure(92, combat_function=do_combat)
        print(result)


if __name__ == "__main__":
    run(main)
