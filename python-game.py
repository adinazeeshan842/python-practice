import random
option = ["rock", "paper", "scissor"]
print("welcome to rock, paper, scissor")

for i in range(1, 4):
    print("Round", i)
    
    computer = random.choice(option)
    user = input("Choose rock, paper or scissor: ")
    
    if user == computer:
        print("it's a tie")
    elif (user=="rock" and computer == "scissor") or (user == "paper" and computer == "rock") or (user == "scissor" and computer == "paper"):
        print("YOU WIN!")
    else:
        print("Computer wins")
    print("Computer chose:", computer)
print("Game Finished")