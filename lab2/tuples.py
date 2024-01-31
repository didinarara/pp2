thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#allow duplicate values
#tuple items can be of any data type

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


thistuple = ("apple",)
print(type(thistuple))
#remember the comma
#NOT a tuple, it is string
thistuple = ("apple")
print(type(thistuple))


tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#tuple can contain different data types


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])



thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")



x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#Convert the tuple into a list to be able to change it, because Tuples are unchangeable



thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#also convert the tuple into a list, add "orange", and convert it back into a tuple



thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
#add tuples


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


'''
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) 
#this will raise an error because the tuple no longer exists
'''



fruits = ("apple", "banana", "cherry")
#Packing a tuple


fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#Unpacking a tuple



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#Assign the rest of the values as a list called "red"



fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)



thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
  
  
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
  
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#joining tuples


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#print the tuple twice


