print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  

x = "Hello"
y = 15
z = ""
c = 0
d = []
e = None
f = False
print(bool(x))
print(bool(y))
print(bool(z))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))


class myclass():
  def __len__(self):
    return 0
obj = myclass()
print(bool(obj))


def myFunction() :
  return True
print(myFunction())


def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")


g = 200
print(isinstance(g, int))