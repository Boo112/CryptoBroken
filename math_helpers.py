
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


def calc_square(numbers):
    result = []
# COMMENT: added just to trigger git diff
    for number in numbers:
        result.append(number*number)
    return result


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result # mod1
    return wrapper

# TODO: refactor this

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper


def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

# TODO: refactor this
# TODO: refactor this

def historical_symbol_ticker_candle(self, start: datetime, end=None, interval=Client.KLINE_INTERVAL_1MINUTE):
        # Convert default seconds interval to string like "1m"
        if isinstance(interval, int):
            interval = str(floor(interval/60)) + 'm'

