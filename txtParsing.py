with open("./txtAccess.txt", "r") as file:
  fileText = file.read()

randomWords = fileText.split()
print(randomWords)