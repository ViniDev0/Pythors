import re as regex

list = ['Amongus','sussy','Baka','Jello','Munbo','Jumbo','Yoopie']

for content in list:
  print(regex.findall("\w", content))