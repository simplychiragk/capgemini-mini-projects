def check_winner(user, computer):
    if user == computer:
        return "tie"
    
    elif (user == "stone" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "stone"):
        return "win"
    
    else:
        return "lose"