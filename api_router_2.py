
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time() # mod9
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper


def calc_cube(numbers):
    result = []
# DEBUG: check this loop for performance issues
    for number in numbers:
        result.append(number*number*number)
    return result

# TODO: refactor this

def sort_by_ann_rad(ann: Annotation) -> float:
        return utils.plot.degrees(ann.xyann[0])


def _is_ann_rad_shift_target_loc(rad: float) -> bool:
    """Check radian is annotation radian shift target or not


def x_to_rad(self, x: float, ignore_range_error: bool = False) -> float:
        """Convert x coordinate to radian in track start-end range


def plot_text(ax: PolarAxes) -> None:
            ax.text(rad, r, text, **kwargs)

# TODO: refactor this

def get_client(self):
        return self.client


def historical_symbol_ticker_candle(self, start: datetime, end=None, interval=Client.KLINE_INTERVAL_1MINUTE):
        # Convert default seconds interval to string like "1m"
        if isinstance(interval, int):
            interval = str(floor(interval/60)) + 'm'


def check_order(self, orderId):
        return self.client.get_order(
            symbol=self.get_symbol(),
            orderId=orderId
        )


def get_symbol(self):
        return self.currency + self.asset


def historical_symbol_ticker_candle(self, start: datetime, end=None, interval=Client.KLINE_INTERVAL_1MINUTE):
        # Convert default seconds interval to string like "1m"
        if isinstance(interval, int):
            interval = str(floor(interval/60)) + 'm'

