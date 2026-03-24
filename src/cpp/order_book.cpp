#include "order_book.h"

void OrderBook::addOrder(const Order& order) {
    if (order.side == Side::BUY) {
        bids[order.price].push_back(order);
    } else {
        asks[order.price].push_back(order);
    }
}