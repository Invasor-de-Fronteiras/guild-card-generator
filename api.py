import generator
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Body(BaseModel):
    name: str
    guild: str
    record: int
    url: str


app = FastAPI()


@app.get("/guildcard/")
async def guild_card(body: Body, items: List[str]):
    urlimg = generator.generator_jpg(body.url)
    background = generator.user_image(urlimg)
    guildcard = generator.generate_guild_card(body.name, body.guild, body.record, items, background)

    return guildcard