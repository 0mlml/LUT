def file_copy(fileA, fileB):
  handleA = open(fileA, 'r')
  handleB = open(fileB, 'w')
  for line in handleA:
    handleB.write(line)
  handleA.close()
  handleB.close()
  print("File copied successfully!")

fileA = input("Please give the name of the source file:\n")
fileB = input("Please give the name of the destination file:\n")

file_copy(fileA, fileB)