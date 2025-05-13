path = "../wordLists/txtAccess.txt"

with open(path, "r") as file:
  file_content = file.read()

words = file_content.split()

def wordCheck(wordList, currentWord):
  counter = 0
  for words in wordList:
    if (words == currentWord):
      counter += 1
  if (counter >= 3):
    return False
  else:
    return True
condition = "Granted" if wordCheck(words, "Apple") == True else "Negated"
print(condition)