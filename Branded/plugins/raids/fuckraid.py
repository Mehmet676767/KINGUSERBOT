from ... import *
from ...modules.mongo.raidzone import *


@app.on_message(cdx(["fr", "rr", "rraid", "fuckraid"]))
@sudo_users_only
async def add_fuck_raid(client, message):
    try:
        aux = await eor(message, "**🔄 yükleniyor....**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**🤖 Bir kullanıcının mesajını yanıtlayın veya kullanıcı adını verin/user_id.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id

        if user_id == message.from_user.id:
            return await aux.edit(
                "**🤣 Ne kadar aptalsın, kendi kimliğine yanıt baskınını etkinleştirmek istiyorsun❓**"
            )
        
        fraid = await add_fuckraid_user(user_id)
        if fraid:
            return await aux.edit(
                "**🤖 Bu Kullanıcıya Yanıt Baskını Başarıyla Eklendi.**"
            )
        return await aux.edit(
            "**🤖 Hey, Raid Bu Kullanıcıda Zaten Etkin Yanıtla❗**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return




@app.on_message(cdx(["dfr", "drr", "drraid", "dfuckraid"]))
@sudo_users_only
async def del_fuck_raid(client, message):
    try:
        aux = await eor(message, "**🔄 yükleniyor...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**🤖 Bir kullanıcının mesajını yanıtlayın veya kullanıcı adını verin/user_id.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id
        
        if user_id == message.from_user.id:
            return await aux.edit(
                "**🤣 Kimliğine Yanıt Baskınını Etkinleştirdiğimde Ne Kadar Aptal❓**"
            )
        
        fraid = await del_fuckraid_user(user_id)
        if fraid:
            return await aux.edit(
                "**🤖 Kimliğine Yanıt Baskınını Etkinleştirdiğimde Ne Kadar Aptal.**"
            )
        return await aux.edit(
            "**🤖 Merhaba, Yanıt Baskını Bu Kullanıcıda Aktif Değil❗**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return
