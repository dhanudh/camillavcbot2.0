from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm Queen music🥰🥰. I am a music bot for playing songs in vc. just add me to your grp make admin and /play <songname>.
        Devoloped by [Kriminal Sri👿](t.me/kriminal_paiya) !**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Founder👿", url="t.me/kriminal_paiya")
                  ],[
                    InlineKeyboardButton(
                        "Vc Assistant🥰", url="t.me/queenbotvc"
                    ),
                    InlineKeyboardButton(
                        "Kriminal Boys👿", url="https://t.me/friends_nagaram/14067"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕", url="https://t.me/stylish_queen_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Founder👿", url="https://t.me/kriminal_paiya")
                ]
            ]
        )
   )
