from binance.client import Client
from models.CCI import CCI
from models.Kline import Kline

class Scanner:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Client(api_key, api_secret)

    def getKlines(self, symbol):
        klines = self.client.get_historical_klines(symbol, Client.KLINE_INTERVAL_5MINUTE, "1 day ago UTC")
        kline_list = list()
        for kline in klines:
            k = Kline(float(kline[1]), float(kline[2]), float(kline[3]), float(kline[4]), float(kline[5]))
            kline_list.append(k)
        return kline_list


    def getCCI(self, symbol, length):
        klines = self.getKlines(symbol)
        cci = CCI(klines, length)
        return cci.value
