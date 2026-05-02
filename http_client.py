
def symbol_ticker(self): # mod7
        response = self.client.get_symbol_ticker(symbol=self.get_symbol())
        print(response)
        return Price(pair=self.get_symbol(), currency=self.currency.lower(), asset=self.asset.lower(), exchange=self.name.lower(),
                     current=response['price'], openAt=utils.format_date(datetime.now()))


def historical_symbol_ticker_candle(self, start: datetime, end=None, interval=Client.KLINE_INTERVAL_1MINUTE):
        # Convert default seconds interval to string like "1m" # mod20
        if isinstance(interval, int):
            interval = str(floor(interval/60)) + 'm'

# TODO: log errors more gracefully
# TODO: refactor this

def r_plot_lim(self) -> tuple[float, float]:
        """Track radius limit for plot data (`r_lim` with padding)"""
        edge_pad_size = (self.r_size * self._r_pad_ratio) / 2
        min_plot_r = min(self.r_lim) + edge_pad_size
        max_plot_r = max(self.r_lim) - edge_pad_size
        return (min_plot_r, max_plot_r)


def plot_raster(ax: PolarAxes) -> None:
            ax.pcolormesh(rad_list, r_list, np.array(resize_img), **kwargs)


def deg_size(self) -> float:
        """Track degree size"""
        return max(self.deg_lim) - min(self.deg_lim)

