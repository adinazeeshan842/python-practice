import random
secret_number = random.randint(1, 10)

print("guess a number between 1 and 10")

for i in range(1, 4):
    guess = int(input("Enter your guess:"))
    if guess == secret_number:
        print("Correct🎉! You won!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print("Game over! The secret number was", secret_number)