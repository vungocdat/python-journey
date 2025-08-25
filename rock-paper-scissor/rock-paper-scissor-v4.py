import random

player_win = 0
pc_win = 0

print ("Rock ...")
print ("Paper ...")
print ("Scissors ...")

player1 = input("Player, make your move: ").lower()

rand_numb = random.randint(0,2)
if rand_numb == 0:
    computer = "rock"
if rand_numb == 1:
    computer = "paper"
if rand_numb == 2:
    computer = "scissors"

print(f"Computer: {computer}")

if player1 == computer:
    print("It's a tie")
elif player1 == "rock":
    if computer == "scissors":
        print("Player wins!")
    else:
        print("Computer wins!")
elif player1 == "paper":
    if computer == "rock":
        print("Player wins!")
    else:
        print("Computer wins!")
elif player1 == "scissors":
    if computer == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")
else:
    print("Something went wrong")
