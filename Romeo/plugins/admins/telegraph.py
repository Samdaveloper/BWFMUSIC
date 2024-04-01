from telegraph import upload_file
from pyrogram import filters
from Romeo import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["tgm" , "Bwftgm" , "Photo" , "link"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("👻ʜᴇʏ ɪ ᴀᴍ🍒 🦋ʙω͠ғ ᴍᴜsɪᴄ ʙᴏᴛ💨")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f' 👤 𝐁σт ᴏᴡɴᴇʀ 𝐍𝐚𝐦𝐞 ༄𝐿 2 𝙍.🖤🜲𝐊𝐈𝐍𝐆❦︎ 𝆺𝅥⃝🍷 @L2R_KING0 . {url}')
