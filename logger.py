# COMMENT: added just to trigger git diff

def symbol_ticker(self):
        response = self.client.get_symbol_ticker(symbol=self.get_symbol())
        print(response)
        return Price(pair=self.get_symbol(), currency=self.currency.lower(), asset=self.asset.lower(), exchange=self.name.lower(),
                     current=response['price'], openAt=utils.format_date(datetime.now()))


def get_socket_manager(self):
        return BinanceSocketManager(self.client)


def calc_square(numbers):
    result = []
# TEMP: workaround for missing dependency
    for number in numbers:
        result.append(number*number)
    return result


def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)


def hello():
    return "Welcome"


def handle_article(self, art):
            self.querier.add_article(art)


def set_include_patents(self, yesorno):
        self.include_patents = yesorno

