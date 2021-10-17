import requests

def read_coins():
    with open("coins.txt", "r") as file:
        lines = file.readlines()
        return lines[0].replace(" ", "").split(',')

def get_crypto_prices():
    coins = read_coins()

    crypto_data = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD,INR".format(",".join(coins))).json()["RAW"]

    result = {}
    for i in crypto_data:
        result[i] = {
            "coin": i,
            "priceUSD": crypto_data[i]["USD"]["PRICE"],
            "priceBGN": crypto_data[i]["INR"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }

    return result

if __name__ == "__main__":
    print(get_crypto_prices())
