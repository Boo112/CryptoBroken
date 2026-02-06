# NOTE: depends on external API response
# DEBUG: check this loop for performance issues
# FIXME: might cause race condition in threads
gg

def __init__(self, key: str, secret: str):
        super().__init__(key, secret)


def cancel_order(self, orderId):
        return self.client.cancel_order(
            symbol=self.get_symbol(),
            orderId=orderId
        )


def start_symbol_ticker_socket(self, symbol: str):
        self.socketManager = self.get_socket_manager()
        self.socket = self.socketManager.start_symbol_ticker_socket(
            symbol=self.get_symbol(),
            callback=self.websocket_event_handler
        )

# TODO: refactor this
