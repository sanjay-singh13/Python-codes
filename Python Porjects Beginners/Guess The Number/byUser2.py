import random
x = int(input())
start = 1
end = x
print(f"Enter a number between 1 and {x}")
while True:
    guess = random.randint(start, end)
    print(f"Is guess {guess} is too high (H), too low (L), or it is correct (C)")
    feedback = input()
    if feedback == 'c':
        print(f"You are right. correct number is {guess}")
        break
    elif feedback == 'h':
        end = guess - 1
    elif feedback == 'l':
        start = guess + 1
    else:
        print("Worng guess. Please guess again")