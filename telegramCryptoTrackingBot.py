import os
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_crypto_prices

command_name = "track"

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

# change to = read_token() if you want to read token from file
telegram_bot_token = os.getenv("TOKEN")

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def track(update, context):
    chat_id = update.effective_chat.id
    message = ""
    crypto_data = get_crypto_prices()

    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        priceUSD = crypto_data[i]["priceUSD"]
        priceBGN = crypto_data[i]["priceBGN"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Coin: {coin}\nPrices: \n\t {priceBGN:,.2f} BGN, \n\t ${priceUSD:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler(command_name, track))
updater.start_polling()