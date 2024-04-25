#include <iostream>
#include <vector>
#include <string>

class ShoppingCart {
private:
    struct CartItem {
        std::string name;
        double cost;
        int quantity;
    };

    std::vector<CartItem> items;

public:
    // Function to add an item to the cart
    void addItem(const std::string& name, double cost, int quantity) {
        CartItem newItem;
        newItem.name = name;
        newItem.cost = cost;
        newItem.quantity = quantity;
        items.push_back(newItem);
        std::cout << "Item added to the cart: " << name << std::endl;
    }

    // Function to remove an item from the cart
    void removeItem(const std::string& name) {
        for (auto it = items.begin(); it != items.end(); ++it) {
            if (it->name == name) {
                items.erase(it);
                std::cout << "Item removed from the cart: " << name << std::endl;
                return;
            }
        }
        std::cout << "Item not found in the cart: " << name << std::endl;
    }

    // Function to calculate the total cost of items in the cart
    double calculateTotalCost() const {
        double totalCost = 0.0;
        for (const auto& item : items) {
            totalCost += item.cost * item.quantity;
        }
        return totalCost;
    }

    // Function to view the items in the cart
    void viewCart() const {
        if (items.empty()) {
            std::cout << "The cart is empty." << std::endl;
        } else {
            std::cout << "Items in the cart:" << std::endl;
            for (const auto& item : items) {
                std::cout << item.name << " - Cost: $" << item.cost << " - Quantity: " << item.quantity << std::endl;
            }
            std::cout << "Total Cost: $" << calculateTotalCost() << std::endl;
        }
    }
};

int main() {
    ShoppingCart cart;

    cart.addItem("Laptop", 1200.00, 2);
    cart.addItem("Smartphone", 500.00, 1);
    cart.viewCart();

    cart.removeItem("Laptop");
    cart.viewCart();

    return 0;
}
