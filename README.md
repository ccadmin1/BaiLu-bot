# Telegram Movie Bot

# BaiLu
</a>  

</p>

<img src="https://telegra.ph/file/94d2c2f6ae8b5bc4436a8.jpg"><br>

## Features

- [x] Auto Filter
- [x] Manuel Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel
- [x] Spelling Check Feature
- [x] File Store

## Variables

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/nj-lJfkgb6w)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/nj-lJfkgb6w)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
### Optional Variables
* `IMDB`: Imdb, the view of information when making True/False.
* `SINGLE_BUTTON`: choose b/w [single or double buttons](https://github.com/josprojects/tgmoviebot/issues/1) True/False.

## larger result buttons
larger results will be better for reading.

* `P_TTI_SHOW_OFF`: Customize Result Buttons to Callback or Url by (True = url / False = callback).
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used separated by space )
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made. Separate multiple IDs by space
* Check [info.py](info.py) for more

## Deploy
You can deploy this bot anywhere.

<details><summary>Deploy to Heroku</summary>
<p>
<br>
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
https://heroku.com/deploy?template=https://github.com/ccadmin1/BaiLu-bot
</details>

<details><summary>Deploy to VPS</summary>
<p>
<pre>
git clone https://github.com/ccadmin1/BaiLu-bot
# Install Packages
pip3 install -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>


## Admin commands
```
• /logs - to get the rescent errors
• /stats - to get status of files in db.
* /filter - add manual filters
* /filters - view filters
* /connect - connect to PM.
* /disconnect - disconnect from PM
* /del - delete a filter
* /delall - delete all filters
* /deleteall - delete all index(autofilter)
* /delete - delete a specific file from index.
* /batch - to create link for multiple posts
* /link - to create link for one post
* /info - get user info
* /id - get tg ids.
* /imdb - fetch info from imdb.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids 
• /index - to add files from a channel
• /leave - to leave from a chat.
• /disable - do disable a chat.
* /enable - re-enable chat.
• /ban_users - to ban a user.
• /unban_users - to unban a user.
• /channel - to get list of total connected channels
• /broadcast - to broadcast a message to all Eva Maria users
```


## Thanks to 
 - Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
 - Thanks To Mahesh For His Awesome [Media-Search-bot](https://github.com/Mahesh0253/Media-Search-bot)
 - Thanks To [Trojanz](https://github.com/trojanzhex) for Their Awesome [Unlimited Filter Bot](https://github.com/TroJanzHEX/Unlimited-Filter-Bot) And [AutoFilterBoT](https://github.com/trojanzhex/auto-filter-bot)
 - Thanks To All Everyone In This Journey

## Disclaimer
[![GNU Affero General Public License 3.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under [GNU AGPL 3.0.](https://github.com/ZauteKm/Dingdi/blob/master/LICENSE)
Selling The Codes To Other People For Money Is *Strictly Prohibited*.
