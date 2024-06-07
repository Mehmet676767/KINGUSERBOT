import os

from ... import *
from pyrogram import filters


@app.on_message(cdz(["😋🥰", "op", "wow", "super", "😋😍"])
    & filters.private & filters.me)
async def self_media(client, message):
    try:
        replied = message.reply_to_message
        if not replied:
            return
        if not (replied.photo or replied.video):
            return
        location = await client.download_media(replied)
        await client.send_document("me", location)
        os.remove(location)
    except Exception as e:
        print("Error: `{e}`")
        return


__NAME__ = "Self"
__MENU__ = f"""
**🥀 Kendinizi İndirin ve Kaydedin\n» Tahrip Edilen Fotoğraf veya Video
Kayıtlı Mesajınıza ✨**

`.op` - Bu Komutu\nKendi Kendini Yok Edenlere Yanıt Vererek Kullanın
Fotoğraf/Video.
**🌿 More Commands:**\n=> [😋🥰, wow, super, 😋😍]
"""
