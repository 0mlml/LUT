def naive_compress(string):
  if len(string) == 0:
    return ""
  resultant = ""
  current = string[0]
  count = 1
  for i in range(1, len(string)):
    if string[i] == current:
      count += 1
    elif count == 1:
      resultant += current
      current = string[i]
    else:
      resultant += current + str(count)
      current = string[i]
      count = 1
  if count == 1:
    resultant += current
  else:
    resultant += current + str(count)
  return resultant

string = input("Give a string to compress:\n")

compressed = naive_compress(string)
print(f"Compressed string: {compressed}\nCompressing ratio {round(len(compressed)/len(string), 2)}")