from ... import *
from pyrogram import filters



import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait

SPAM_CHATS = []


@app.on_message(
    filters.command(["utag", "stag", "tags", "mtag"], prefixes=["/", "@"])
     & ~filters.private
)
@sudo_users_only
async def tag_all_users(_, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "durdurmak istiyorsanız tgging işlemi zaten çalışıyor, bu yüzden kullanın /cancel yada /bitir /stop "
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** Beğendiğiniz herkesi etiketlemek için biraz metin verin ÖRNEK »** `@utag MERHABA`"
        )
        return
    if replied:
        try:
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})"
                if usernum == 14:
                    await app.send_message(
                        message.chat.id,
                        f"{replied.text}\n\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""

        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        try:
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})"
                if usernum == 14:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass



@app.on_message(
    filters.command(
        [
            "dur",
            "cancel",
            "bitir",
            "stop",
            "mentionoff",
            "cancelall",
        ],
        prefixes=["/", "@"],
    )
     & ~filters.private
)
@sudo_users_only
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("**Etiketleme işlemi başarıyla durduruldu!**")

    else:
        await message.reply_text("**iyide iki gözüm etiket atmıyorum ki😅!**")
        return
