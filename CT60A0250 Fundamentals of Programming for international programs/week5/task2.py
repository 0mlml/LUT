def count_words(sentence):
  return len(sentence.split())

sentence = input("Give a sentence:\n")
print(f"This sentence contains {count_words(sentence)} words.")