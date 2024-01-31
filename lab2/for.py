fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)



for x in "banana":
  print(x)



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#print with banana and stop



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#print without banana 



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)



for x in range(6):
  print(x)
#it is the same as:
'''
x = 0
while x<6 :
    print(x)
    x += 1
'''



for x in range(2, 6):
  print(x)



for x in range(2, 30, 3):
  print(x)
#increments the sequence by 3, while default is 1



for x in range(6):
  print(x)
else:
  print("Finally finished!")
  


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#else will not be executed due to breaking loop



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
    

for x in [0, 1, 2]:
  pass
#pass statement to avoid getting an error