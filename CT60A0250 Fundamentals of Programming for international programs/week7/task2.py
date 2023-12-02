def print_names(file_name):
  handle = open(file_name, 'r')
  names = handle.readlines()
  handle.close()
  for name in sorted(names):
    print(name.strip())

file_name = input("Give the name of the input file:\n")
print_names(file_name)