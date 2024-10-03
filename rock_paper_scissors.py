import random

print("Welcome to Rock Paper Scissors!")
user_score = 0
comp_score = 0

while(True):
    user_input = input("Enter E to start/continue or Q to quit: ")
    print()
    if user_input.upper() == "Q":
        print("Summary: ")
        print(f"Your score: {user_score}")
        print(f"Computer score: {comp_score}")
        break
    else:
        rps_dict = {1: "Rock", 2:"Paper", 3:"Scissors"}
        comp_choice = random.randrange(1,4)

        while(True):
            user_choice = input("Choose Rock, Paper or Scissors (1 for Rock, 2 for Paper, 3 for Scissors): ")
            if(user_choice != "1" and user_choice != "2" and user_choice != "3"):
                print("Please enter a number from 1 to 3\n")
            else:
                user_choice = int(user_choice)
                break

        print(f"You play {rps_dict[user_choice]}.")
        print(f"Computer plays {rps_dict[comp_choice]}.")

        if user_choice == comp_choice:
            print("Draw")
        elif user_choice - comp_choice == 1 or user_choice - comp_choice == -2:
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            comp_score += 1

        print()

            
