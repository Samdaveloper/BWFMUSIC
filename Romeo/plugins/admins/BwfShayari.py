from Romeo import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **✨बहुत अच्छा लगता है तुझे सताना और फिर प्यार से तुझे मनाना।🍃** ",
           " **⚚‎•👁मेरी जिंदगी मेरी जान हो तुम मेरे सुकून का दुसरा नाम हो तुम।👻** ",
           " **🕊⃟♥️तुम मेरी वो खुशी हो जिसके बिना, मेरी सारी खुशी अधूरी लगती है।*🍃* ",
           " **ᴛᴏᴏᴛᴇ 💔 ʜᴜʏᴇ ᴅɪʟ ɴᴇ ʙʜɪ ᴜsᴋᴇ** ",
           " **❤🥀अगर एक हारा हुआ इंसान◑❃हारने के बाद भी🌸🍃** ",
           " **🥀🍃मुस्कूरा दे....❁✥◓❤🌸🍃तो जितने वाला भी जीत कि खुशी खो देता है...!!🌸** ",
           " **🌸❤आंखों से अश्कों की बरसात हो गई✨** ",
           " **🥀गम की हमसे ऐसी मुलाकात हो गई🌸** ",
           " **༎🍁༎𝆺𝅥जो लोग दिल के अच्छे होते है ना🥀⍣⃪͜𓆪** ",
           " **🥀🍃*दिमाग वाले उन्ही का फायदा उठाते हे🦋** ",
           " **🍃🥀🌸🌸❤‍🩹इश्क सभी को जीना सीखा देता है,❤‍🩹❤🌸🥀🍃** ",
           " **❤अगर आए तुम्हे हिचकियाँ,❤‍🩹** ",
           " **🌸क्योंकि इस दिल को आदत है,🌸** ",
           " **🥀🍃🌸🌸𝗘𝗸 𝗴𝗮𝗹𝘁𝗶 𝗿𝗼𝗷 𝗸𝗿 𝗿𝗵𝗲 𝗵𝗮𝗶 𝗵𝗮𝗺. 😌🌸🌸** ",
           " **❤मैं भी बैलेंटाइन डे मनाऊँगा.....💌  ** ",
           " **🍷जिन लड़कियों ने मुझे माना किया है.....👁** ",
           " **🦋उनकी माँ बाप को फ़ोन करके.....💨** ",
           " **🙊उनकी लोकेशन बताऊँगा👻** ",
           " **💔👑🌷मालूम होती फ़ितर तुम्हारी तो हम इतना इश्क़ नहीं करते🍃🥀💌** ",
           " **🥀🌹🍃तुम जिस्म के शौकीन हों हमको कैसे समझते 💔🌸🍃** ",
           " **👀❣️🌸आँखें तो ठीक है मे  तो रूह तक रोयी है🍷🖇🎭** ",
           " **🌸🥀🍃𝐎𝐲𝐞𝐞 𝐭𝐞𝐫𝐞 𝐛𝐚𝐚𝐝 𝐡𝐮𝐦 𝐭𝐞𝐫𝐢 𝐭𝐫𝐡 𝐤𝐢𝐬𝐢 𝐤𝐨 𝐜𝐡𝐚𝐡𝐞𝐧𝐠𝐞 𝐧𝐡𝐢🫠❤️** ",
           " **❤दिल ना दुखायेंगे कभी..🎀 🍒ना छोड़ के जायेंगे🥀** ",
           " **♦️हर चीज से बडकर.💌🍷सिर्फ तुझको चाहेंगे.....👁** ",
           " **🍷बहुत उदास है कोई तेरे जाने से 👻** ",
           " **❣️हो सके तो लौट आ किसी बहाने से🦋** ",
           " **🍃तू लाख खफा सही, मगर एक बार तो देख 👑** ",
           " **🍷कोई टूट गया है तेरे रूठ जाने से !😭💌** ",
           " ***~✦ !!❤‍🩹  दिल🌍 से 🖇️प्यार 👻किया🍁 है ** ",
           " **दिल 👀से🖤 ही 💞निभायेगे 😇जब🤍 तक💝जिंदा🤔 है❤️ तुझे😘 ही 🤗चाहेंगे🫶🏻✨!!** ",
           " **मोहतरमा आप बहुत खूबसूरत हो आंखो 🙄में काजल लगाया करो...** ",
           " **💌खुद से भी ज्यादा किसी की इज्जत की थी🌷** ",
           " **🥀हमने भी दिल लगाने की हिम्मत की थी👻** ",
           " **❣️बस किस्मत के हाथों से हर गए वरना 🦋** ",
           " **❅ Phone काट मम्मी आ गई क्या। 😆** ",
           " **❅ और भाबी से कब मिल वा रहे हो । 😉** ",
           " **❅ क्या आप मुझसे प्यार करते हो 💚** ",
           " **❅ मैं तुम से बहुत प्यार करती हूं..? 👀** ",
           " **❅ बेबी एक kiss दो ना..?? 🙉** ",
           " **❅ एक जॉक सुनाऊं..? 😹** ",
           " **❅ vc पर आओ कुछ दिखाती हूं  😻** ",
           " **❅ क्या तुम instagram चलते हो..?? 🙃** ",
           " **❅ whatsapp नंबर दो ना अपना..? 😕** ",
           " **❅ आप की दोस्त से मेरी सेटिंग करा दो ..? 🙃** ",
           " **❅ सारा काम हो गया हो तो ऑनलाइन आ जाओ।..? 🙃** ",
           " **❅ कहा से हो आप 😊** ",
           ]

BWF_TAG = [
           " **🍷जिन लड़कियों ने मुझे माना किया है.....👁** ",
           " **🦋उनकी माँ बाप को फ़ोन करके.....💨** ",
           " **🙊उनकी लोकेशन बताऊँगा👻** ",
           " **💔👑🌷मालूम होती फ़ितर तुम्हारी तो हम इतना इश्क़ नहीं करते🍃🥀💌** ",
           " **🥀🌹🍃तुम जिस्म के शौकीन हों हमको कैसे समझते 💔🌸🍃** ",
           " **👀❣️🌸आँखें तो ठीक है मे  तो रूह तक रोयी है🍷🖇🎭** ",
           " **🌸🥀🍃𝐎𝐲𝐞𝐞 𝐭𝐞𝐫𝐞 𝐛𝐚𝐚𝐝 𝐡𝐮𝐦 𝐭𝐞𝐫𝐢 𝐭𝐫𝐡 𝐤𝐢𝐬𝐢 𝐤𝐨 𝐜𝐡𝐚𝐡𝐞𝐧𝐠𝐞 𝐧𝐡𝐢🫠❤️** ",
           " **❤दिल ना दुखायेंगे कभी..🎀 🍒ना छोड़ के जायेंगे🥀** ",
           " **♦️हर चीज से बडकर.💌🍷सिर्फ तुझको चाहेंगे.....👁** ",
           " **🍷बहुत उदास है कोई तेरे जाने से 👻** ",
           " **❣️हो सके तो लौट आ किसी बहाने से🦋** ",
           " **🍃तू लाख खफा सही, मगर एक बार तो देख 👑** ",
        ]


@app.on_message(filters.command(["Shayaritag", "Lovetag", "Pyartag", "shaaditag", ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. ")

    if message.reply_to_message and message.text:
        return await message.reply("/Hinditag")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/Shayaritag")
    else:
        return await message.reply("/Shayaritag")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. ")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["cancel", "offtag", "Shayariofftag", "lovetag", "stop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠 𝐁𝐚𝐛𝐲.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ ≛ 🄸🥂Gʀᴏᴜᴘꨄ︎[❣️]™✺🕊️⃝🔥 ♦")
