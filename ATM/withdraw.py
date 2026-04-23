import balance

def withdraw():
    amount = float(input("Enter the amount to withdraw: "))
    if 0 >= amount:
        print("Invalid amount. Please enter a positive number less than or equal to your balance.")
    elif amount > balance.balance:
        print("Insufficient funds. Please enter an amount less than or equal to your balance.")
    else:        
        balance.balance -= amount
        print(f"You have withdrawn ${amount}. Your new balance is: ${balance.balance}")
        