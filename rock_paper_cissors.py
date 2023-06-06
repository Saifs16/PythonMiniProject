import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("The computer picked", computer_pick +".")

    if user_input == "rock" and computer_pick == "scissors":
        user_wins +=1
        print("You win!")
    elif user_input == "paper" and computer_pick == "rock":
        user_wins +=1
        print("You win!")
    elif user_input == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("You win!")
    else:
        computer_wins += 1
        print("You Lost!")

print("You won",user_wins,"time \nThe computer won", computer_wins, "times")
print("Goodbye!")