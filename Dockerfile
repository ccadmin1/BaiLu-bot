FROM python:3.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip freeze > requirements.txt
RUN mkdir /BaiLu-bot
WORKDIR /BaiLu-bot
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
