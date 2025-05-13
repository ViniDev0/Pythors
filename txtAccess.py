addingContent = input("Add Stuff: ")
with open("./txtAccess.txt", "w") as file:
  readableText = file.write(addingContent)

    
with open("./txtAccess.txt", "r") as file:
  display = file.read()

print(display)