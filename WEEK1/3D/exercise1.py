def items_to_restock(inventory, threshold):

    restock_list = []
    for item, quantity in inventory.items():
        if quantity < threshold:
            restock_list.append(item)
    return restock_list

inventory = {
    "pens": 5,
    "notebooks": 0,
    "erasers": 12,
    "markers": 3,

}

result = items_to_restock(inventory, 6)
print("Items to restock:", result)