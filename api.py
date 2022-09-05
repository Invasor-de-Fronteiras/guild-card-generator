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


@app.post("/items/")
async def create_item(body: Body, items: List[str]):
    urlimg = generator.generator_jpg(body.url)
    background = generator.user_image(urlimg)
    generator.generate_guild_card(body.name, body.guild, body.record, items,background)
    print(body.awards)

    return body