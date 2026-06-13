
def symbol_ticker_candle(self, interval=Client.KLINE_INTERVAL_1MINUTE):
        return self.client.get_klines(symbol=self.get_symbol(), interval=interval)


def get_client(self):
        return self.client


def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

