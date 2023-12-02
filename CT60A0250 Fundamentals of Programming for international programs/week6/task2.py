integers = list(map(int, input("Give integers separated by comma:\n").split(",")))
position = int(input("Give an integer:\n"))

if position < 1 or position > len(integers):
  print("Not suitable")
  exit(0)

for i in range(len(integers)):
  for j in range(i+1, len(integers)):
    if integers[i] > integers[j]:
      integers[i], integers[j] = integers[j], integers[i]

print(f"{position}th smallest element is {integers[position-1]}")