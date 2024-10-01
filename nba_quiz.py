print("Welcome to NBA 2023-24 Quiz!")
playing = input("Type Yes to Enter the Game: ")

if playing.lower() == "yes":
    print("Okay! Let's Play :)")
    score = 0

    answer1 = input("1. Who won the Most Valuable Player (MVP) Award? ")
    if "Jokic" in answer1:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Nikola Jokic.")

    answer2 = input("2. Which team won the Championship? ")
    if "Celtics" in answer2:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Boston Celtics.")

    answer3 = input("3. Who won Defensive Player of the Year (DPOY) Award? ")
    if "Gobert" in answer3:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Rudy Gobert.")

    answer4 = input("4. Who had the most triple doubles? ")
    if "Sabonis" in answer4:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Domantas Sabonis.")

    answer5 = input("5. Who was the first coach to be fired? ")
    if answer5 == "Stephen Silas":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Stephen Silas.")

    if score >= 4:
        statement = "Congrats!"
    elif score >= 2:
        statement = "Good Job!"
    else:
        statement = "Try harder next time!"
    print(f"You had a score of {str(score)}/5. {statement}")