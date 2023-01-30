import random

def play_game(n):
	computer_choice = random.randint(1, 100)
	chance = n
	game_on = True

	while game_on:
		user_guess = int(input("Guess a Number "))
		if user_guess == computer_choice:
			game_on = False
			print("Correct")
		elif user_guess > computer_choice and chance > 0:
			print("Too High")
			chance -= 1
			print(f"Chances left = {chance}")
		elif user_guess < computer_choice and chance > 0:
			print("Too Low")
			chance -= 1
			print(f"Chances left = {chance}")

diff = 0

difficulty = input("Hard or Easy?").lower()
if difficulty == "hard":
	diff = 5
elif difficulty == "easy":
	diff = 10
play_game(diff)