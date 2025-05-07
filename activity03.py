loginInput = input("Username:")
passwordInput = input("PassKey:")

login = "admin01"
password = "8080443A21"

# From my experience ONLY incorrect passwords should be alerted as wrong. For security purposes i will ommit the login case. 

if loginInput == login and passwordInput == password:
  print("Login access granted")

elif loginInput == login and passwordInput != password:
  print("Access Denied, Incorrect Password!")

else:
  print("Access Denied")