from order import Order
from order_book import OrderBook
from matcher import Matcher

ob = OrderBook()
matcher = Matcher(ob)

matcher.process_order(Order(1, "SELL", 95, 5))
matcher.process_order(Order(2, "SELL", 100, 5))

matcher.process_order(Order(3, "BUY", 100, 8))

print("\nFinal Order Book:")
print(ob)

matcher.process_order(Order(10, "BUY", 90, 5))
matcher.process_order(Order(11, "SELL", 95, 5))

print("\nBefore cancellation:")
print(ob)

ob.cancel_order(2)

print("\nAfter cancellation:")
print(ob)