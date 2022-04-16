class script(object):
    SERCH_MOVIE = """𝐇𝐢 {},
നിങ്ങൾക്ക് ആവശ്യമുള്ള സിനിമകൾ ഇവിടെ നിന്ന് എടുക്കാം. 

 ɴʙ: DVD ഇറങ്ങിയാൽ മാത്രമേ സിനിമകൾ ലഭിക്കൂ 😜"""
    CMD_LIST = """𝐇𝐢 {},
• /id - get id of a specifed user. 
 • /info  - get information about a user. 
 • /imdb  - get the film information from IMDb source. 
 • /search  - get the film information from various sources. 
 • /whois :-give a user full details 

 ᴛʜɪs ɪs ғᴏʀ ᴀᴅᴍɪɴs 

• /logs - to get the rescent errors 
• /stats - to get status of files in db. 
• /delete - to delete a specific file from db. 
• /users - to get list of my users and ids. 
• /chats - to get list of the my chats and ids 
• /leave  - to leave from a chat. 
• /disable  -  do disable a chat. 
• /ban  - to ban a user. 
• /unban  - to unban a user. 
• /channel - to get list of total connected channels 
 • /broadcast - to broadcast a message to all users. 
 • /connect  - connect a particular chat to your PM. 
• /disconnect  - disconnect from a chat. 
• /connections - list all your connections. 
• /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members. 
• /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message. 
• /filter - add a filter in chat. 
• /filters - list all the filters of a chat. 
• /del - delete a specific filter in chat. 
• /delall - delete the whole filters in a chat (chat owner only)"""
    BOT_TXT = """𝐇𝐢 {},
➪ എങ്ങനെ നിങ്ങൾക്ക് ഈ ബോട്ട് പ്രവർത്തിപ്പിക്കാം
 
➪ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ. 

/update - മെയിൻ ചാനലിൽ ജോയിൻ ചെയ്യാനുള്ള ലിങ്ക് വേണമെങ്കിൽ ഈ കമാൻഡ് ഉപയോഗിക്കാം 😀"""
    UPDATE_CMD = """𝐇𝐢 {}, 
➪ ബോട്ട് പ്രവർത്തിക്കണമെങ്കിൽ താഴെ കാണുന്ന മെയിൻ ചാനലിൽ ജോയിൻ ചെയ്യുക. 

➪ എന്തിനാണ് മെയിൻ ചാനലിൽ ജോയിൻ ചെയ്യുന്നത് എന്ന് നിങ്ങൾക്ക് സംശയം തോന്നാം, കാരണം മെയിൻ ചാനലിന്റെ ലിങ്ക് സ്ഥിരമായിരിക്കും, ഈ ചാനലിൽ കൂടിയാണ് ബോട്ട് അപ്ഡേറ്റ്സും മൂവി ചാനലിന്റെ ലിങ്കും ഇടുന്നത്. 

➪ മറ്റു ചാനലുകളെ അപേക്ഷിച്ചു മെയിൻ ചാനലിന് കോപ്പിറൈറ് വരുന്നതിനുള്ള സാധ്യയത കുറവാരിക്കും 😀"""
    START_TXT = """Hᴇʏ {} {},
Mʏ ɴᴀᴍᴇ ɪꜱ <a href=https://t.me/{}>{}</a>, I ᴀᴍ ᴊᴜsᴛ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ Aᴜᴛᴏғɪʟᴛᴇʀ Bᴏᴛ Wɪᴛʜ ᴇxᴛʀᴀ ᴄᴀᴘᴀʙɪʟɪᴛɪᴇs.Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ ᴀɴᴅ I'ʟʟ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴛʜᴇʀᴇ 😍

➪ /bot - ബോട്ടിനെ കുറിച്ചും ഇത് ഉപയോഗിക്കേണ്ടരീതിയെക്കുറിച്ചറിയാൻ ഈ കമാൻഡ് ഉപയോഗിക്കാവുന്നതാണ് 😀"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """► 𝐌𝐲 𝐍𝐚𝐦𝐞: {}
► 𝐋𝐢𝐛𝐫𝐚𝐫𝐲: Pyrogram
► 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞: MongoDB
► 𝐒𝐞𝐫𝐯𝐞𝐫: Heroku"""

    SOURCE_TXT = """<b>NOTE:</b>
- This is an open source project. 

<b>╔══ 𝘑𝘰𝘪𝘯 ★ 𝘚𝘩𝘢𝘳𝘦 ★ 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 ══╗
♻️ ᴊᴏɪɴ :- <a href=https://t.me/+7AyTKA_SqdsyNWNl><b>⚜️ Backup Channel ⚜️</b></a>
♻️ ᴊᴏɪɴ :- <a href=https://t.me/KC_Films><b>🔰 Main Group 🔰</b></a>
♻️ ᴊᴏɪɴ :- <a href=https://t.me/KC_Filmz><b>🧲 Backup Group 🧲</b></a>
╚══ 𝘑𝘰𝘪𝘯 ★ 𝘚𝘩𝘢𝘳𝘦 ★ 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 ══╝</b>

 
<b>💘 Team ➜ <a href=https://t.me/KCFilmss>💫 KC Filmss 💫</a>\n✯ ━━━━━ ✧ ━━━━━ ✯</b>\n"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. KC Eva Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    """Help: <b>Buttons</b>

- This Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. KC Eva Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/KCFilmss)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """► 𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬: <code>{}</code>
► 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: <code>{}</code>
► 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐚𝐭𝐬: <code>{}</code>
► 𝐔𝐬𝐞𝐝 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: <code>{}</code>"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
