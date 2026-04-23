def user_choice():
    print("Please choose one of the following options:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        return "stone"
    elif choice == '2':
        return "paper"
    elif choice == '3':
        return "scissors"
    elif choice == '4':
        return "exit"
    else:
        print("Invalid choice. Please try again.")
        return user_choice()