from pyrogram import filters
from TheApi import api

from config import LOG_GROUP_ID
from YukkiMusic import app
from SafoneAPI import SafoneAPI


@app.on_message(filters.command("advice"))
async def advice(_, message):
    A = await message.reply_text("...")
    res = api.get_advice()
    await A.edit(res)


@app.on_message(filters.command("astronomical"))
async def advice(_, message):
    a = await SafoneAPI().astronomy()
    if a["success"]:
        c = a["date"]
        url = a["imageUrl"]
        b = a["explanation"]
        caption = f"Today's [{c}] astronomical event:\n\n{b}"
        await message.reply_photo(url, caption=caption)
    else:
        await message.reply_photo("try after some time")
        await app.send_message(LOG_GROUP_ID, "/astronomical not working")


__MODULE__ = "Device"
__HELP__ = """<blockquote><b>
/advice - Get random advice
/astronomical - to get today's astronomical  fact</b></blockquote>"""
