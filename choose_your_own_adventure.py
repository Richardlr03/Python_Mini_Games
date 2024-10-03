name = input("Enter your Name: ")
print(f"Welcome, {name}, to this adventure!")

answer = input("You are chased by a group of gangsters. You arrive at a T-junction and you can go left, right, or climb over the wall. What is your choice? ")

if answer.lower() == "left":
    answer = input("You met an old man. Do you want to seek help from him? Type yes or no: ").lower()
    if answer == "yes":
        print("Unfortunately, the old man is the gangster boss. You lose!")
    else:
        print("The old man shoot you. You lose!")

elif answer.lower() == "right":
    answer = input("There is a river in front of you. Do you want to swim across or run along the shore? Type swim or walk: ").lower()
    if answer == "swim":
        print("The river is full of alligators. You lose!")
    else:
        asnwer = input("The gangsters are still searching for you. You can decide to hide on a tree ot behing the bush. Type tree or bush: ").lower()
        if answer == "tree":
            print("There is a bee hive on the tree. You get stung by a poisonous bee and died. You lose!")
        else:
            print("The gangsters can't find you and give up. You win!")
else:
    print("The wall is too high, you can't climb over. You are caught. You lose!")