from models.Scanner import Scanner

s = Scanner("api_key", "api_secret")
SYMBOLS = ["BNBBTC", "ETHBTC", "TRXBTC", "LTCBTC", "BTTBTC"]

for SYMBOL in SYMBOLS:
    cci = s.getCCI(SYMBOL, 50)
    if cci > 100:
        print(SYMBOL + " CCI: " + str(round(cci,1)))

