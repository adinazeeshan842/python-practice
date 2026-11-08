
import random

words = ["python", "apple", "computer", "school", "coding"]

secret_word = random.choice(words)

print("Welcome to Word Guessing Game!")
print("Guess the secret word!")

for i in range(1, 4):

    guess = input("Enter your guess: ").lower()

    if guess == secret_word:
        print("Correct! You won!")
        break
    else:
        print("Wrong guess! Try again.")

else:
    print("Game over!")
    print("The word was:", secret_word)

