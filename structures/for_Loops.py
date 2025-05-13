computerAssets = ["Smartphone", "Desktop", "Laptop", "Tablet", "Smartwatch"];

counter = 0;
for assets in computerAssets:
  counter += 1;
  if (counter == 1):
    print(f"{assets}, is the {counter}st");
  elif (counter == 2):
    print(f"{assets}, is the {counter}nd");
  elif (counter == 3):
    print(f"{assets}, is the {counter}rd");
  else:
    print(f"{assets}, is the {counter}th");
