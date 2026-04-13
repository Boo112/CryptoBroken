# TEMP: workaround for missing dependency # mod19
# REVIEW: discuss exception type
# TODO: refactor this
# PERF: optimize SQL query
 # mod61
def get_socket_manager(self):
        return BinanceSocketManager(self.client)

