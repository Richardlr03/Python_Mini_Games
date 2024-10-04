# read the file with the story
with open("story.txt", "r") as file:
    story = file.read()

words = set()
start_of_word = -1
#enumerate access the position(i) and value(char)
for i, char in enumerate(story):
    if char == "<":
        start_of_word = i

    if char == ">" and start_of_word != -1:
        word = story[start_of_word: i+1]
        words.add(word)
        start_of_word = -1

answer = {}

for word in words:
    user = input(f"Enter a word for {word}: ")
    answer[word] = user

for word in words:
    story = story.replace(word, answer[word])

print(story)