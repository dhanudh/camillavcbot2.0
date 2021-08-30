from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ  ɢʀᴏᴜᴩ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. 
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜsɪᴄ ғʀᴇᴇʟʏ 🤗 Developed By [Kriminal Sri👿](https://t.me/kriminal_paiya) !**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Founder👿", url="t.me/kriminal_paiya")
                  ],[
                    InlineKeyboardButton(
                        "Vc Assistant🥰", url="queenbotvc"
                    ),
                    InlineKeyboardButton(
                        "Kriminal Boys👿", callback_data="Kriminal_boys"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕", url="https://t.me/camillamusicbot?startgroup=true"
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

@run_async
def Kriminal_boys(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "Kriminal_boys":
        query.message.edit_text(
            text="""[KRIMINAL SRI👿](t.me/kriminal_paiya)
            [KRIMINAL KISHORE](t.me/kriminal_paiyan)
            [KRIMINAL DHANUSH](t.me/boss_of_the_telegram)
            [KRIMINAL SANTHOSH](t.me/naan_konjam_420)
            [KRIMINAL MUKESH](t.me/immukesh_10)
            [KRIMINAL SAI](t.me/attitudeking007)
            [KRIMINAL MOULY](t.me/afrozmouly)
            [KRIMINAL MUJA](t.me/muja46)
            [KRIMINAL SAB](t.me/mr_sab_sj) """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True
