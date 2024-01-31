i = 1
while i < 6:
  print(i)
  i += 1
#print form 1 to 5
  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#print till 3

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#print withot 3 till 6

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")