import bisect


class OrderBook:
    def __init__(self):
        self.bids = {}
        self.asks = {}

        self.bid_prices = []  # descending
        self.ask_prices = []  # ascending

        self.order_map = {}

    def add_order(self, order):
        self.order_map[order.id] = order

        if order.side == "BUY":
            if order.price not in self.bids:
                self.bids[order.price] = []
                bisect.insort(self.bid_prices, -order.price)

            self.bids[order.price].append(order)

        elif order.side == "SELL":
            if order.price not in self.asks:
                self.asks[order.price] = []
                bisect.insort(self.ask_prices, order.price)

            self.asks[order.price].append(order)

    def get_best_bid(self):
        if not self.bid_prices:
            return None
        best_price = -self.bid_prices[0]
        return self.bids[best_price][0]

    def get_best_ask(self):
        if not self.ask_prices:
            return None
        best_price = self.ask_prices[0]
        return self.asks[best_price][0]

    def remove_order(self, order):
        if order.side == "BUY":
            price_level = self.bids.get(order.price, [])
            if order in price_level:
                price_level.remove(order)
                if not price_level:
                    del self.bids[order.price]
                    self.bid_prices.remove(-order.price)

        elif order.side == "SELL":
            price_level = self.asks.get(order.price, [])
            if order in price_level:
                price_level.remove(order)
                if not price_level:
                    del self.asks[order.price]
                    self.ask_prices.remove(order.price)

        if order.id in self.order_map:
            del self.order_map[order.id]

    def cancel_order(self, order_id):
        if order_id not in self.order_map:
            print(f"Order {order_id} not found")
            return

        order = self.order_map[order_id]
        self.remove_order(order)
        print(f"Cancelled Order {order_id}")

    def __repr__(self):
        return f"BIDS: {self.bids}\nASKS: {self.asks}"