from ... import *
from ...modules.mongo.streams import *
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound


@app.on_message(cdx(["dur", "pause"]) & ~filters.private)
@sudo_users_only
async def pause_stream(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if a.status == "playing":
            await call.pause_stream(chat_id)
            await eor(message, "**Akış Duraklatıldı!**")
        elif a.status == "son", "dur":
            await eor(message, "**Zaten Duraklatıldı!**")
        elif a.status == "oynamıyorum":
            await eor(message, "**Hiçbir Şey Yayınlanmıyor!**")
    except GroupCallNotFound:
        await eor(message, "**VC'de değilim!**")
    except Exception as e:
        print(f"Error: {e}")


@app.on_message(cdz(["cpse", "cson", "cpause"]))
@sudo_users_only
async def pause_stream_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "**🥀 Yayın Sohbet Seti Yok❗**"
    )
    try:
        a = await call.get_call(chat_id)
        if a.status == "şarkı başladı":
            await call.pause_stream(chat_id)
            await eor(message, "**akış durduruldu!**")
        elif a.status == "paused":
            await eor(message, "**akış zaten durdururldu!**")
        elif a.status == "oynamıyorum":
            await eor(message, "**akış kapalı lütfen sesliyi açın!**")
    except GroupCallNotFound:
        await eor(message, "**VC'de değilim!**")
    except Exception as e:
        print(f"hata: {e}")

  
