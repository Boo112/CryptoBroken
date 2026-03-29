# QUESTION: is this behavior expected?

def order(self, order: Order):
        return self.client.create_order(
            symbol=order.symbol,
            side=order.side,
            type=order.type,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=order.quantity,
            price=order.price
        )


def get_asset_balance(self, currency):
        response = self.client.get_asset_balance(currency)
        return response['free']
# TODO: support retry mechanism

