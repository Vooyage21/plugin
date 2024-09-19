import random

import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from YukkiMusic import app


@app.on_message(filters.command(["wall", "wallpaper"]))
async def wall(_, message: Message):

    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        text = None
    if not text:
        return await message.reply_text("`Please give some query to search.`")
    m = await message.reply_text("sᴇᴀʀᴄʜɪɴɢ...")
    try:
        url = requests.get(f"https://api.safone.dev/wall?query={text}").json()[
            "results"
        ]
        ran = random.randint(0, 7)
        await message.reply_photo(
            photo=url[ran]["imageUrl"],
            caption=f"🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("ʟɪɴᴋ", url=url[ran]["imageUrl"])],
                ]
            ),
        )
        await m.delete()
    except Exception as e:
        await m.edit_text(
            f"`ᴡᴀʟʟᴘᴀᴘᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ : `{text}`",
        )


__MODULE__ = "Wall"
__HELP__ = """<blockquote><b>
**COMMANDS:**

• /WALL - **download and send wallpaper.**

**INFO:**

- this bot provides a command to download and send wallpaper.
- use /WALL command with a text to search for wallpaper and send it to the chat.

**NOTE:**

- this command can be used to download and send wallpaper.</b></blockquote>
"""
