import random
x = int(input())
print(f"Guess a number between 1 and {x}")
number = random.randint(1,x)
while True:
    guess = int(input())
    if guess == number:
        print(f"You are right. correct number is {guess}")
        break
    elif guess > number:
        print("guess is too high...guess a smaller number")
    elif guess < number:
        print("guess is too low...guess a larger number")
    else:
        print("Worng guess. Please guess again")