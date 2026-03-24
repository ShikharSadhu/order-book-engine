class OrderBook:
    def __init__(self):
        self.bids = []  # buy orders
        self.asks = []  # sell orders

    def add_order(self, order):
        if order.side == "BUY":
            self.bids.append(order)
            self.bids.sort(key=lambda o: (-o.price, o.timestamp))
        elif order.side == "SELL":
            self.asks.append(order)
            self.asks.sort(key=lambda o: (o.price, o.timestamp))

    def get_best_bid(self):
        return self.bids[0] if self.bids else None

    def get_best_ask(self):
        return self.asks[0] if self.asks else None

    def __repr__(self):
        return f"BIDS: {self.bids}\nASKS: {self.asks}"