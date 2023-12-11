import random

random.seed(42)

while True:
    u = input("Rock, Paper, Scissors (type 'Exit' to quit):\n")
    if u == "Exit":
        break
    c = ["Rock", "Paper", "Scissors"][random.randint(0, 2)]
    if u not in ["Rock", "Paper", "Scissors"]:
        print("That's not a valid play. Check your spelling!")
        continue
    print("It was a tie!") if u == c else print(f"You lost! {u} loses to {c}") if (u == "Rock" and c == "Paper") or (u == "Paper" and c == "Scissors") or (u == "Scissors" and c == "Rock") else print(f"You won! {u} triumphs {c}")
