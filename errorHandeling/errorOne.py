while True:
  try:
    post = int(input("Enter a Number"))
    break
  except ValueError:
    valueErrorMessage = "Invalid Number, try again"
    print(valueErrorMessage)