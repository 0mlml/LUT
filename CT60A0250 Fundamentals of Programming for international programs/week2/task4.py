word = input("Give a word:\n")
print(f"The length of the word is {len(word)}")
num = int(input(f"Give an integer smaller than or equal to {len(word)}:\n")) - 1
print(f"{word[:num]}*{word[num+1:]}")