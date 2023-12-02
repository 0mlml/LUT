import csv 

filename = input("Give the name of the CSV file:\n")

with open(filename, 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    print(row[1].strip())

