#pragma once

#include <cstdint>

enum class Side {
    BUY,
    SELL
};

struct Order {
    int id;
    Side side;
    int price;
    int quantity;

    // pointers for linked list (VERY IMPORTANT)
    Order* next;
    Order* prev;

    // constructor
    Order(int id_, Side side_, int price_, int quantity_)
        : id(id_), side(side_), price(price_), quantity(quantity_),
          next(nullptr), prev(nullptr) {}
};