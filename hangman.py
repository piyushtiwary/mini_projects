import requests

data = requests.get(url="https://random-word-api.herokuapp.com/word").json()

string = data[0]
life = 6

li = []
for i in range(len(string)):
    li += "_"


def displayField():
    for i in range(len(string)):
        print(li[i], end=" ")


displayField()
gameOn = True


def playGame():
    global life
    guess = input("Guess a Letter").lower()
    count = 0
    for ch in string:
        if ch == guess:
            li[count] = guess

        count += 1

    displayField()
    if guess not in string:
        life -= 1


while "_" in li:
    playGame()
    print("\n Life Left", life)
    if life == 0:
        print("You Lose")
        break
