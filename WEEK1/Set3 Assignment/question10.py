#SIMPLE BANK ACCOUNT SIMULATOR
def process_transactions(starting_balance, transactions):
    
    balance = starting_balance
    failed = []

    for transaction in transactions:

        if transaction["type"] == "deposit":

            balance = balance + transaction["amount"]

        elif transaction["type"] == "withdraw":

            if balance >= transaction["amount"]:

                balance = balance - transaction["amount"]

            else:

                failed.append(transaction)

    result = {
        "final_balance": balance,
        "failed_transactions": failed
    }

    return result


transactions = [
    {"type": "deposit", "amount": 200},
    {"type": "withdraw", "amount": 100},
    {"type": "withdraw", "amount": 500}
]

print(process_transactions(300, transactions))