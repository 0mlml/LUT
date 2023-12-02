s = input("Enter a string:\n")

print("Modified string: ", end="")
for i in range(len(s)):
    if s[i] == "s":
        print("z", end="")
    elif s[i] == "S":
        print("Z", end="")
    else:
        print(s[i], end="")