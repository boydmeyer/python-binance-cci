from models.Scanner import Scanner

s = Scanner("test", "test")
SYMBOLS = ["BNBBTC", "ETHBTC", "TRXBTC", "LTCBTC", "BTTBTC"]

for SYMBOL in SYMBOLS:
    cci = s.getCCI(SYMBOL, 50)
    if cci > 100:
        print(SYMBOL + " CCI: " + str(round(cci,1)))

