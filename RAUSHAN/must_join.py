from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            # 🔥 LINK FIX
            if str(MUST_JOIN).startswith("@"):
                link = f"https://t.me/{MUST_JOIN.replace('@','')}"
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link

                # अगर invite link None आया तो नया बना लो
                if not link:
                    link = await bot.export_chat_invite_link(MUST_JOIN)

            try:
                await msg.reply_photo(
                    photo="https://i.ibb.co/N2rCpDHD/x.jpg",
                    caption=f"✦ » ғɪʀsᴛʟʏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ғᴀᴍɪʟʏ ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ [˹ ᴏꜰꜰɪᴄᴇ ˼]({link}). ᴀғᴛᴇʀ ᴊᴏɪɴ ❖ /start ❖ ᴍᴇ ᴀɢᴀɪɴ 🌹!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("˹ ᴊᴏɪɴ ᴏꜰꜰɪᴄᴇ ˼", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
