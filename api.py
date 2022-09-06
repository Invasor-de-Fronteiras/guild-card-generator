import generator
from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from typing import List
from io import BytesIO





app = FastAPI()


@app.post("/guildcard/")
async def guild_card(user: str, guild: str, record: int, url: str, items: List[str]= Query(None)):
    urlimg = generator.generator_jpg(url)
    background = generator.user_image(urlimg)
    guildcard = generator.generate_guild_card(user, guild, record, items, background)

    filtered_image = BytesIO()
    guildcard.save(filtered_image, "PNG")
    filtered_image.seek(0)

    return StreamingResponse(filtered_image, media_type="image/png")