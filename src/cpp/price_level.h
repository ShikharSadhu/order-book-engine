#pragma once

#include "order.h"

struct PriceLevel {
    int price;

    Order* head;  // first order (oldest)
    Order* tail;  // last order (newest)

    PriceLevel(int price_) : price(price_), head(nullptr), tail(nullptr) {}

    // add order to end (FIFO)
    void add_order(Order* order) {
        order->next = nullptr;
        order->prev = tail;

        if (tail) {
            tail->next = order;
        } else {
            head = order;
        }

        tail = order;
    }

    // remove specific order (O(1))
    void remove_order(Order* order) {
        if (order->prev) {
            order->prev->next = order->next;
        } else {
            head = order->next;
        }

        if (order->next) {
            order->next->prev = order->prev;
        } else {
            tail = order->prev;
        }

        order->next = nullptr;
        order->prev = nullptr;
    }

    // get first order (best priority)
    Order* get_head() {
        return head;
    }

    bool empty() {
        return head == nullptr;
    }
};