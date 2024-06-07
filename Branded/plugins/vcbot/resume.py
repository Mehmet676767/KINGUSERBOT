from ... import *
from ...modules.mongo.streams import *
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound


@app.on_message(cdx(["rsm", "devam", "resume"]) & ~filters.private)
@sudo_users_only
async def resume_stream(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if a.status == "paused":
            await call.resume_stream(chat_id)
            await eor(message, "**akış dewam ediyor!**")
        elif a.status == "oynuyorum":
            await eor(message, "**akış zaten dewam ediyor!**")
        elif a.status == "dewam eden bir akiş yok":
            await eor(message, "**sesli kapalı!**")
    except GroupCallNotFound:
        await eor(message, "**seste değilim!**")
    except Exception as e:
        print(f"Error: {e}")


@app.on_message(cdz(["crsm", "cdewam", "cresume"]))
@sudo_users_only
async def resume_stream_chat(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "**🥀 No Stream Chat Set❗**"
    )
    try:
        a = await call.get_call(chat_id)
        if a.status == "paused":
            await call.resume_stream(chat_id)
            await eor(message, "**Stream Resumed!**")
        elif a.status == "playing":
            await eor(message, "**Already Playing!**")
        elif a.status == "not_playing":
            await eor(message, "**Nothing Streaming!**")
    except GroupCallNotFound:
        await eor(message, "**I am Not in VC!**")
    except Exception as e:
        print(f"Error: {e}")

  
