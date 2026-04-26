import balance
import transactions
def withdraw():
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive number less than or equal to your balance.")
    elif amount > balance.balance:
        print("Insufficient funds. Please enter an amount less than or equal to your balance.")
    else:        
        balance.balance -= amount
        transactions.transactions_list.append(f"Withdrawal: ${amount}")
        print(f"You have withdrawn ${amount}. Your new balance is: ${balance.balance}")
        