class OrderBook:
    def __init__(self):
        self.bids = []  # buy orders
        self.asks = []  # sell orders
        self.order_map = {}

    def add_order(self, order):
        self.order_map[order.id] = order

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
    def cancel_order(self, order_id):
        if order_id not in self.order_map:
            print(f"Order {order_id} not found")
            return

        order = self.order_map[order_id]

        if order.side == "BUY":
            self.bids.remove(order)
        elif order.side == "SELL":
            self.asks.remove(order)

        del self.order_map[order_id]

        print(f"Cancelled Order {order_id}")
    
    def remove_order(self, order):
        if order.side == "BUY":
            if order in self.bids:
                self.bids.remove(order)
        elif order.side == "SELL":
            if order in self.asks:
                self.asks.remove(order)

        if order.id in self.order_map:
            del self.order_map[order.id]