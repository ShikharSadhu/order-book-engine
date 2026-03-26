from order_book import OrderBook

class Matcher:
    def __init__(self, order_book):
        self.order_book = order_book

    def process_order(self, order):
        if order.side == "BUY":
            self._match_buy(order)
        elif order.side == "SELL":
            self._match_sell(order)

    def _match_buy(self, order):
        while order.quantity > 0:
            best_ask = self.order_book.get_best_ask()

            if not best_ask:
                break

            if order.price < best_ask.price:
                break

            trade_quantity = min(order.quantity, best_ask.quantity)

            print(f"TRADE: {trade_quantity} @ {best_ask.price}")

            order.quantity -= trade_quantity
            best_ask.quantity -= trade_quantity

            if best_ask.quantity == 0:
                self.order_book.remove_order(best_ask)

        if order.quantity > 0:
            self.order_book.add_order(order)

    def _match_sell(self, order):
        while order.quantity > 0:
            best_bid = self.order_book.get_best_bid()

            if not best_bid:
                break

            if order.price > best_bid.price:
                break

            trade_quantity = min(order.quantity, best_bid.quantity)

            print(f"TRADE: {trade_quantity} @ {best_bid.price}")

            order.quantity -= trade_quantity
            best_bid.quantity -= trade_quantity

            if best_bid.quantity == 0:
                self.order_book.remove_order(best_bid)
        if order.quantity > 0:
            self.order_book.add_order(order)