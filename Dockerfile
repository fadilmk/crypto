FROM python:3.9

RUN pip install python-telegram-bot

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD python /app/telegramCryptoTrackingBot.py