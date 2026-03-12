# TEMP: workaround for missing dependency
# REVIEW: discuss exception type
# TODO: refactor this

def get_socket_manager(self):
        return BinanceSocketManager(self.client)

