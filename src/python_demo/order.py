import time

class Order:
    def __init__(self, order_id, side, price, quantity):
        self.id = order_id
        self.side = side  # "BUY" or "SELL"
        self.price = price
        self.quantity = quantity
        self.timestamp = time.time()

    def __repr__(self):
        return f"Order(id={self.id}, side={self.side}, price={self.price}, quantity={self.quantity}, time={self.timestamp})"