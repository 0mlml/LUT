def anagram(A,B):
  return sorted(A) == sorted(B)

strA = input("Enter string A:\n")
strB = input("Enter string B:\n")

print(f"{strA} and {strB} are {'not ' if not anagram(strA,strB) else ''}anagrams")