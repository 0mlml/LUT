import string
import random

random.seed(8292)

while True:
    length = int(input("Enter the length of the password: "))
    if length <= 0:
        print("Password length must be a positive integer.")
    else:
        print(f"Generated password: {''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))}")
