import random

while True:
    user_action = input("Enter a choice in lowercase(rock, paper, scissors, lizard, spock): ")
    possible_actions = ["scissors", "paper", "rock", "lizard", "spock"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("(and as it always has) Rock crushes scissors! You win!")
        if computer_action == "lizard":
            print("Rock crushes lizard! You win!")
        if computer_action == "spock":
            print("Spock vaporizes rock! You lose!")
        if computer_action == "paper":
            print("Paper covers rock! You lose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        if computer_action == "lizard":
            print("Lizard eats Paper! You lose!")
        if computer_action == "spock":
            print("Paper disproves spock! You win!")
        if computer_action == "scissors":
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        if computer_action == "lizard":
            print("Scissors decapitates lizard! You win!")
        if computer_action == "spock":
            print("Spock smashes Scissors! You lose!")
        if computer_action == "rock":
            print("(and as it always has) Rock crushes scissors! You lose.")
    elif user_action == "spock":
        if computer_action == "paper":
            print("Paper disproves Spock! You lose!")
        if computer_action == "rock":
            print("Spock vaporizes rock! You win!")
        if computer_action == "scissors":
            print("Spock smashes Scissors! You win!")
        if computer_action == "lizard":
            print("Lizard poisons spock! You lose!")
    elif user_action == "lizard":
        if computer_action == "paper":
            print("Lizard eats paper! You win!")
        if computer_action == "rock":
            print("Rock crushes lizard! You lose!")
        if computer_action == "scissors":
            print("Scissors decapitates lizard! You Lose!")
        if computer_action == "spock":
            print("Lizard poisons spock! You win!")
    else:
        print("My sensors tell me your illiterate or can't read directions, try again...")
