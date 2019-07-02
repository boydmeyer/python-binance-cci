from builtins import len
class CCI:
    def __init__(self, klines, length):
        TP = self.getTypicalPrice(klines[-1])
        SMA = self.getTypicalPriceSMA(klines[-length:])
        MD = self.getMeanDeviation(SMA, klines[-length:])
        self.value = (TP-SMA)/(0.015*MD)

    def getTypicalPrice(self, kline):
        return (kline.high + kline.low + kline.close)/3

    def getTypicalPriceSMA(self, klines):
        sum = 0
        for k in klines:
            sum += self.getTypicalPrice(k)
        return sum / len(klines)

    def getMeanDeviation(self, SMA, klines):
        total = 0
        for k in klines:
            TP = self.getTypicalPrice(k)
            x = TP - SMA
            if(x < 0):
                x = -x
            total += x
        return total/len(klines)