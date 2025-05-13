path = "../wordLists/txtAccess.txt"
with open(path, "r") as file:
  fileText = file.read()

randomWords = fileText.split()
print(randomWords)