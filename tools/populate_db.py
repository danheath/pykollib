import asyncio
from tortoise import Tortoise

from aiohttp import ClientSession
from libkol import models

import items, equipment, monsters, consumables, zapgroups, foldgroups, npcstores, trophies, effects, bonuses, skills, outfits, familiars


async def populate():
    await Tortoise.init(
        db_url="sqlite://../libkol/libkol.db", modules={"models": models}
    )

    await Tortoise.generate_schemas(safe=True)

    async with ClientSession() as session:
        print("Inserting items")
        await items.load(session)

        print("Inserting monsters")
        await monsters.load(session)

        print("Inserting familiars")
        await familiars.load(session)

        print("Inserting skills")
        await skills.load(session)

        print("Discovering equipable items")
        await equipment.load(session)

        print("Discovering consumable items")
        await consumables.load(session)

        print("Discovering zappable items")
        await zapgroups.load(session)
        print("Discovering foldable items")
        await foldgroups.load(session)
        print("Discovering outfits")
        await outfits.load(session)

        print("Discovering store items")
        await npcstores.load(session)

        print("Inserting trophies")
        await trophies.load(session)

        print("Inserting effects")
        await effects.load(session)

        print("Inserting bonuses")
        await bonuses.load(session)

    await Tortoise.close_connections()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(populate())
    loop.close()
