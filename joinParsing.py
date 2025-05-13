with open("./txtAccess.txt", "r") as file:
  updates = file.read()
updates = updates.split()

updates = "\n".join(updates)
with open("./txtAccess.txt", "w") as file:
  file.write(updates)

print(updates)