from time import sleep as eeepy;

maxDevices = 5;
i = 1;

while i < maxDevices:
  balance = maxDevices - i; 
  print(f"Addition devices can be connected {balance}");
  i += 1;
  eeepy(0.5);
print("User reached maximum number of connections.")