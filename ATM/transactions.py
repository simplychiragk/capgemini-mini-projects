
transactions_list = []

def display_transactions():
    if transactions_list == 0:
        print("No transactions found.")
    else:
        for t in transactions_list:
            print(t)