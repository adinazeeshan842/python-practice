import random

print("Welcome to Heads or Tails!")

choices = ["heads", "tails"]

computer = random.choice(choices)

user = input("Choose heads or tails: ")

print("Result:", computer)

if user == computer:
    print("You won!")
else:
    print("You lost!")

