thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#lists allow duplicate values


thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#Print the number of items in the list


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1)
print(list2)
print(list3)
print(list4)
#List items can be of any data type


mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#What is the data type of a list?


thislist = ["apple", "banana", "cherry"]
print(thislist[1])



thislist = ["apple", "banana", "cherry"]
print(thislist[-1])



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#Change the second item



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"



thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#Change the second value by replacing it with two new values



thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#Change the second and third value by replacing it with one value



thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#Insert "watermelon" as the third item



thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)



thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)



thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)




thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#it will remove the first occurance of "banana"




thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#removes the specified index
#if you do not specify the index, the pop() method removes the last item



thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

'''
thislist = ["apple", "banana", "cherry"]
del thislist
#Delete the entire list
'''


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#The list still remains, but it has no content


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
  

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])



thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]




fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)



newlist = [x for x in range(10)]
print(newlist)
#print numbers till 9


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)
#replace all values with 'hello'



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
#replace banana with orange



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#sort the list alphabetically
#can do the same with numbers in increasing order


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#in decreasing order(can do with words too)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#Sort the list based on how close the number is to 50


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#will check uppercased words first


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#Perform a case-insensitive sort of the list



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#reverse the order



thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#make a copy


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#also make a copy with the list() method


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#join two lists


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
#also join them


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
#again joining




