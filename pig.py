import random

def roll_dice():
    score = 0
    while(True):
        choice = input(f"Would you like to roll? (y): ").lower()
        if choice != "y":
            break

        dice = random.randrange(1,7)
        if dice == 1:
            print(f"You rolled {dice}. You lose all your points!")
            score = 0
            break
        else:
            score += dice
            print(f"You rolled {dice}.")

        print(f"Your round score is {score}.") 

    return score


print("Welcome to Pig Game!")

while(True):
    num = input("Enter the number of players: ")

    if num.isdigit() == False:
        print("Please enter a number.")
    else:
        num = int(num)
        if num <= 1:
            print("Please enter a number greater than 1.")
        else:
            print(f"{num} players entering the game....\n")
            break

max_score = 50
scores_list = [0 for i in range(num)]

while max(scores_list) < max_score:

    for i in range(num):
        print(f"Player {i+1}'s turn.")
        print(f"Your current total score is {scores_list[i]}\n")

        score = roll_dice()
        
        scores_list[i] += score
        print(f"Player {i+1}'s total score is {scores_list[i]}.\n")

max_score = max(scores_list)
max_score_list = []
max_count = 0
for index in range(len(scores_list)):
    if scores_list[index] == max_score:
        max_count += 1
        max_score_list.append(index+1)

if max_count == 1:
    winning_player = scores_list.index(max_score)
    print(f"Player {winning_player+1} wins with {max_score} points!")
else:
    max_players = ",".join(max_score_list)
    print(f"Player {max_players} are tied with {max_score} points.")
    print("Tiebreak Round!\n")

    tiebreak_list = []
    for num in max_score_list:
        print("Player {num}'s turn.")
        score = roll_dice()

        tiebreak_list.append((num, score))

    max_score = 0
    for player, score in tiebreak_list:
        if score >= max_score:
            max_score = score
            max_player = player

    print(f"Player {max_player} wins with {max_score} points!")