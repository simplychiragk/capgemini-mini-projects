import balance
import withdraw
import deposit

def atm():
    while True:
        print("\n----------------------- ATM MENU -----------------------")
        print("\nWelcome to the ATM!")    
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        print()

        option = input("Enter your choice: ")

        if option == '1':
            balance.check_balance()

        elif option == '2':
            withdraw.withdraw()

        elif option == '3':
            deposit.deposit()

        elif option == '4':
            print("Thank you for using the ATM. Goodbye!")
            break  # THIS is what actually exits

        else:
            print("Invalid option. Try again.")

atm()