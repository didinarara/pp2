thisset = {"apple", "banana", "cherry"}
print(thisset)
#Sets are unordered, so you cannot be sure in which order the items will appear
#Once a set is created, you cannot change its items, but you can remove items and add new items



thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#Duplicate values will be ignored


thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#True and 1 is considered the same value
#False and 0 is considered the same value


thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#Get the number of items in a set


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
#Set items can be of any data type



thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#Using the set() constructor to make a set



thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)



thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#prints True



thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)




thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#Add elements from tropical into thisset



thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)




thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# If the item to remove does not exist, remove() will raise an error




thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#the same as remove
#but If the item to remove does not exist, discard() will NOT raise an error




thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
#this method will remove a random item




thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#empties the set



'''
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists
'''



set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#The union() method returns a new set with all items from both sets




set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#The update() method inserts the items in set2 into set1



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#Keep the items that exist in both set x, and set y
#apple



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
#the same as above




x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
#Keep All, But NOT the Duplicates


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
#the same as above



