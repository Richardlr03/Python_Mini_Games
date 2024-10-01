import random

print("Welcome to the Number Guessing Game!")
diff = input("Choose your difficulty (1 for Easy, 2 for Medium, 3 for Hard): ")

while(diff != "1" and diff != "2" and diff != "3"):
    print("Please input a number from 1 to 3 to select difficulty!")
    diff = input("Choose your difficulty (1 for Easy, 2 for Medium, 3 for Hard): ")

low = 1
up = 10**(int(diff)+1)

ans = random.randrange(low,up+1)
count = 0

while(True):
    guess = input(f"Guess the Number from {low} to {up}: ")
    if guess.isdigit():
        guess = int(guess)
        if guess < low or guess > up:
            print("Please enter a number within the range.")
        else:
            count += 1
            if guess == ans:
                print("You are correct!")
                break
            elif guess > ans:
                print("Wrong! You are above the number.")
                up = guess
            else:
                print("Wrong! You are below the number.")
                low = guess
    else:
        print("Please enter a number!")

print(f"You solved this game in {count} guesses!")