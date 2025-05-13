from time import sleep as nightyNight
list = ['Zello','Jello','Mello','Bello','Nello']
countdown = 0
for content in list:
  if content == 'Bello' and countdown == 3:
    print(f"{content}, Human!")
  else:
    countdown += 1
    nightyNight(0.5)
    print(countdown)