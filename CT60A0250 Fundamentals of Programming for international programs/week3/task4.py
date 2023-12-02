word1 = input("Enter word 1:\n")
word2 = input("Enter word 2:\n")

if word1 == word2:
    print("The words are the same.")
elif word1 < word2:
    print(f"'{word1}' comes earlier in order than '{word2}'.")
else:
    print(f"'{word2}' comes earlier in order than '{word1}'.")

found = False
if 'z' in word1:
    print(f"Letter 'z' is found in word '{word1}'.")
    found = True
if 'z' in word2:
    print(f"Letter 'z' is found in word '{word2}'.")
    found = True

if not found:
    print("The letter 'z' was not found in either of the words.")

word3 = input("Enter a word to be tested:\n")
if word3 == word3[::-1]: 
    print(f"'{word3}' is a palindrome.")
else:
    print(f"'{word3}' is not a palindrome.")
