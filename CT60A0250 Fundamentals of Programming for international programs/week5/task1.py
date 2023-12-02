def occurrences(ch, string):
  c = 0
  for i in range(len(string)):
    if string[i] == ch:
      c += 1
  return c

ch = input("Enter a character:\n")
if len(ch) != 1:
  print("Error: Give a single character.")
  exit(0)
string = input("Enter a string:\n")
print(f"The character '{ch}' appears {occurrences(ch, string)} time(s) in the string.")
