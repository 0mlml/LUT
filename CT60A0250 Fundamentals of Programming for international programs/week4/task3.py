s = input("Enter a string:\n")

vowels = 0
for i in range(len(s)):
    if s[i].lower() in "aeiou":
        vowels += 1

print(f"Number of vowels is: {vowels}")