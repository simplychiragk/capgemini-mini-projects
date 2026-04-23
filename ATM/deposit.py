import balance

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        balance.balance += amount
        print(f"You have deposited ${amount}. Your new balance is: ${balance.balance}")
    else:
        print("Invalid amount. Please enter a positive number.")