def cart_total(cart):
    total = 0

    for item in cart:
        price = cart[item]["price"]
        quantity = cart[item]["quantity"]

        if quantity > 0:
            total = total + (price * quantity)

    return total


cart = {
    "apple": {"price": 10, "quantity": 4},
    "bread": {"price": 2.5, "quantity": 2},
    "milk": {"price": 1.2, "quantity": 3}
}

print(cart_total(cart))