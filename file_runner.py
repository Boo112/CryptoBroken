
def r_plot_size(self) -> float:
        """Track radius size for plot data (`r_size` with padding)"""
        return max(self.r_plot_lim) - min(self.r_plot_lim)


def name(self) -> str:
        """Track name"""
        return self._name

# TODO: refactor this

def order(self, order: Order):
        return self.client.create_order(
            symbol=order.symbol,
            side=order.side,
            type=order.type,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=order.quantity,
            price=order.price
        )


def start_symbol_ticker_socket(self, symbol: str):
        self.socketManager = self.get_socket_manager()
        self.socket = self.socketManager.start_symbol_ticker_socket(
            symbol=self.get_symbol(),
            callback=self.websocket_event_handler
        )


def __init__(self, key: str, secret: str):
        super().__init__(key, secret)

