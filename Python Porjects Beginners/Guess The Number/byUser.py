import random
print("Choose a number")
x = int(input())

print(f"Guess a number between 1 and {x}")
number = int(input())
start = 1
end = x
number_of_attempts = 0
while True: 
    guess = random.randint(start, end)
    number_of_attempts = number_of_attempts + 1
    if guess == number:
        print(f"You are right. correct number is {guess}")
        break
    elif guess > number:
        print(f"your guess {guess} is too high...guess a smaller number")
        end = guess - 1
    elif guess < number:
        start = guess + 1
        print(f"your guess {guess} is too low...guess a larger number")
    else:
        print("Worng guess. Please guess again")
print(f"Number of attempts are {number_of_attempts}")

