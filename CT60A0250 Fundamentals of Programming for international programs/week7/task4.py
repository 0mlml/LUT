file_name = input("Give the text file to analyze:\n") 

with open(file_name, 'r') as file:
  line_count = 0
  word_count = 0
  
  for line in file:
    line_count += 1
    words = line.split()
    word_count += len(words)
    
  print(f"Number of lines: {line_count}")
  print(f"Number of words: {word_count}")