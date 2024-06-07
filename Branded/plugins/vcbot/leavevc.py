from asyncio.queues import QueueEmpty
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound

from ... import *
from ...modules.mongo.streams import *
from ...modules.utilities import queues


@app.on_message(cdx(["lve", "ayril", "leave", "leavevc"]) & ~filters.private)
@sudo_users_only
async def leave_vc(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if (a.status == "oynamıyorum"
            or a.status == "oynuyorum"
            or a.status == "durdum"
        ):  
            try:
                queues.clear(chat_id)
            except QueueEmpty:
                pass
            await call.leave_group_call(chat_id)
            await eor(message, "**Sol VC!**")
    except GroupCallNotFound:
        await eor(message, "**VC'de değilim!**")
    except Exception as e:
        print(f"Error: {e}")


@app.on_message(cdz(["clve", "cleave", "cleavevc"]))
@sudo_users_only
async def leave_vc_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "**🥀 Yayın Sohbet Seti Yok❗**"
    )
    try:
        a = await call.get_call(chat_id)
        if (a.status == "oynamıyorum"
            or a.status == "oynuyorum"
            or a.status == "durdum"
        ):  
            try:
                queues.clear(chat_id)
            except QueueEmpty:
                pass
            await call.leave_group_call(chat_id)
            await eor(message, "**Left VC!**")
    except GroupCallNotFound:
        await eor(message, "**I am Not in VC!**")
    except Exception as e:
        print(f"Error: {e}")
