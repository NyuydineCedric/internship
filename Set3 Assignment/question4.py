#NESTED ORDER SUMMARY

def order_summary(orders):
    
    summary = {}

    for customer in orders:

        total = 0

        for order in orders[customer]:
            total = total + (order["price"] * order["quantity"])

        summary[customer] = total

    return summary


def top_spender(orders):

    summary = order_summary(orders)

    highest_name = ""
    highest_total = 0

    for customer in summary:
        if summary[customer] > highest_total:
            highest_total = summary[customer]
            highest_name = customer

    return highest_name


orders = {
    "Alice": [
        {"item": "pen", "price": 1.5, "quantity": 3}
    ],
    "Bob": [
        {"item": "book", "price": 12, "quantity": 1},
        {"item": "pen", "price": 1.5, "quantity": 2}
    ]
}

print(order_summary(orders))
print(top_spender(orders))