def validator(login, password):
  attempts = 0
  attemptsLimit = 2
  while (attempts < attemptsLimit):
    
    if login == 'admin01' and password == "8080":
      print(f"Access Granted, {login}")
      return
    else:
      attempts += 1
      getDataUsername()
      getDataPasskey()
    if attempts >= attemptsLimit:
      print("Access Denied due to attempts deplention")
def getDataUsername():
  username = input("Username: ")

  return username

def getDataPasskey():
  key = input("Password: ")
  
  return key


login = getDataUsername()
password = getDataPasskey()
validator(login, password)
