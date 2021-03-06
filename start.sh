
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/ccadmin1/BaiLu-bot /BaiLu-bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /BaiLu-bot
fi
cd /BaiLu-bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
