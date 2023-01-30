import random

word_list = ["APPLE", "CAKE", "HANGMAN", "RIVER", "JAZZ", "UPPER", "LOWER", "MONSTER", "TRUCK"]

num = random.randint(1,9)
string = word_list[num]
life = 6

li = []
for i in range(len(string)):
	li +="_"

def displayField():
	for i in range(len(string)):
		print(li[i],end =" ")

displayField()
gameOn = True


def playGame():
	global life
	guess = input("Guess a Letter").upper()
	count = 0
	for ch in (string):
		if ch==guess:
			li[count]=guess
			count +=1
		else:
			count +=1
	displayField()
	if guess not in string:
		life -= 1

while "_" in li:
	playGame()
	print("\n Lifes Left" ,life)
	if life == 0:
		print("You Lose")
		break
