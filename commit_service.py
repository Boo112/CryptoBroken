# TEMP: workaround for missing dependency # mod19
# REVIEW: discuss exception type
# TODO: refactor this # mod82
# PERF: optimize SQL query
 # mod61
def get_socket_manager(self):
        return BinanceSocketManager(self.client)

# TODO: refactor this

def hello():
    return "Welcome"

# CLEANUP: remove debug print before commit

def get_items(code: int):
    return { 'discount_amount': coupon_code.get(code) }


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

