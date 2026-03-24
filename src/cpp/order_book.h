class OrderBook {
public:
    void addOrder(const Order& order);

private:
    std::map<int, std::list<Order>, std::greater<int>> bids;
    std::map<int, std::list<Order>> asks;
};