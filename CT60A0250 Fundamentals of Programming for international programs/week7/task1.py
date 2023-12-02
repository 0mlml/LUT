def write_names(file_name):
  handle = open(file_name, 'w')
  current = input("Enter a name or 'stop':\n")
  while current != "stop":
    handle.write(current + "\n")
    current = input("Enter a name or 'stop':\n")
  handle.close()

file_name = input("Enter the name of the file to be saved:\n")
write_names(file_name)