def includes(substring, string):
  for i in range(len(string)):
    if string[i] == substring[0]:
      if string[i:i+len(substring)] == substring:
        return True
  return False

first = input("Enter the first string:\n")
second = input("Enter the second string:\n")

print(f"The first string can{'not' if not includes(first, second) else ''} be found in the second string.")