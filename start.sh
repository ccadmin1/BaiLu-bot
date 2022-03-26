if [ -z $UPSTREAM_REPO ]

then

  echo "Cloning main Repository"

  git clone https://github.com/ccadmin1/BaiLu.git /BaiLu

else

  echo "Cloning Custom Repo from $UPSTREAM_REPO "

  git clone $UPSTREAM_REPO /BaiLu

fi

cd /BaiLu

pip3 install -U -r requirements.txt

echo "BaiLu bot runing...."

python3 main.py
