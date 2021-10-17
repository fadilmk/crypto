# TelegramCryptoTracker
Simple bot that tracks current crypto prices on command. Bot is written with Python. CryptoCompare API is the data source for the bot.
By default the bot is showing information about current crypto prices in BGN & USD and also what were changes in percentage for the last 1h and 24h.

Initial idea and solution came out from [this article by Section.io](https://www.section.io/engineering-education/cryptocurrency-tracking-telegram-bot/)
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
In order to run/host the bot, you need to have valid token from [BotFather](https://core.telegram.org/bots). 
You can check this [simplified guide](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0)

In order to run the project, make sure you have **Python** installed. The project has been tested with **version 3.7 & 3.9**

For easier work you can use some Python exe if you need to debug. The one used for project development is:
* **PyCharm 2020** - built and tested it, the project should also be running on any newer version as long as it supports the above mentioned frameworks

### Installation / Usage

If you want to run the bot, you need to adjust it's configuration. There are 2 key files used for adjusting the bot. In them you can configure: 
* **Token** provided by BotFather should be added either in ENV variables OR [token.txt](TelegramCryptoTracker/token.txt) file. By default we're using env vars, but this can be changes inside [telegramCryptoTrackingBot.py](TelegramCryptoTracker/telegramCryptoTrackingBot.py)
* **List of coints** can be adjusted in [coins.txt](TelegramCryptoTracker/coins.txt) file.

**NOTE**: The token inside token.txt has been revoked, it's staying there just so that users can get an idea of what to insert.

Also, **if you want to change the default currencies** you can do so in [tracker.py](TelegramCryptoTracker/tracker.py) inside crypto_data url

### Defaults: 
**List of coins**(can be changed): 
```
BTC, ETH, LTC, XRP, ADA, DOT, XLM, BNB, XTZ
```
**Currencies**(can be changed): 
```
USD, BGN
```

### Bot Commands
The bot is triggered by a single command that can be changed inside [telegramCryptoTrackingBot.py](TelegramCryptoTracker/telegramCryptoTrackingBot.py)

**/track**-> type this command in a shared chat with the bot and it will print current prices

## Support

<a href="https://www.buymeacoffee.com/i.ganchosov" target="_blank">☕ Buying me a coffee is great way to show support if you find this project useful.</a>

## CryptoTrackingBot example message
![CryptoTrackerExampleMessage](https://github.com/Plotso/TelegramCryptoTracker/blob/main/CryptoTrackerExampleMessage.PNG?raw=true)