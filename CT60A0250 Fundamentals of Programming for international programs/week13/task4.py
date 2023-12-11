import random

random.seed(0)

b = [' '] * 9
p = f = (random.randint(0, 1) + 1) % 2

print(f" Your symbol is {'X' if p == 0 else 'O'}.")
print("You go first.") if p == 0 else None

if p == 1:
    s = random.choice([i for i in range(9) if b[i] == ' '])
    b[s] = 'X'
    p = 0

while True:
    print(f"\n {b[0]} | {b[1]} | {b[2]}\n---+---+---\n {b[3]} | {b[4]} | {b[5]}\n---+---+---\n {b[6]} | {b[7]} | {b[8]}\n")
    if len([i for i in range(9) if b[i] == ' ']) == 0:
        print("Draw!")
        break
    if p == 0:
        s = int(input("Pick an open slot:\n")) - 1
        if s > 8 or s < 0 or b[s] != ' ':
            print("That's not an open slot.")
            continue
        b[s] = 'X' if f == 0 else 'O'
        if any(all(b[i] == ('X' if f == 0 else 'O') for i in c) for c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]):
            print(f"\n {b[0]} | {b[1]} | {b[2]}\n---+---+---\n {b[3]} | {b[4]} | {b[5]}\n---+---+---\n {b[6]} | {b[7]} | {b[8]}\n")
            print("You win!")
            break
        p = 1
    if p == 1:
        if len([i for i in range(9) if b[i] == ' ']) == 0:
            continue
        s = random.choice([i for i in range(9) if b[i] == ' '])
        b[s] = 'X' if f == 1 else 'O'
        if any(all(b[i] == ('X' if f == 1 else 'O') for i in c) for c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]):
            print(f"\n {b[0]} | {b[1]} | {b[2]}\n---+---+---\n {b[3]} | {b[4]} | {b[5]}\n---+---+---\n {b[6]} | {b[7]} | {b[8]}\n")
            print("You lose!")
            break
        p = 0

input("Press Enter to continue...")