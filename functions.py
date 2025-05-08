def validator():
  attempts = 0
  attemptsLimit = 3
  while (attempts < attemptsLimit):
    login = getDataUsername()
    password = getDataPasskey()
    if login == 'admin01' and password == 8080:
      print(f"Access Granted, {login}")
      return
    attempts += 1
    if attempts >= attemptsLimit:
      print("Access Denied due to attempts deplention")
def getDataUsername():
  username = input("Username: ")

  return username

def getDataPasskey():
  key = int(input("Password:"))
  
  return key


validator()
