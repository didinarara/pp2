x = 5
y = 10
print(x + y)
print(y - x)
print(x * y)
print(y / x)
print(y % x)
print(x ** y)
print(y // x)

a = 5
a &= 3  #AND
print(a)
b = 5
b |= 3  #OR
print(b)
c = 5
c ^= 3  #XOR
print(c)
d = 5
d >>= 3
print(d)
e = 5
e <<= 3
print(e)

z = 5
print(z > 3 and z < 10)
print(z > 3 or z < 4)
print(not(z > 3 and z < 10))

q = 1
r = 2
print(q is r)
print(q is not r)

x = ["apple", "banana"]
print("banana" in x)
print("pineapple" not in x)

print(~3)      #inverts each bit
print(3 << 2)  #shift left by pushing zeros
print(8 >> 2)  #shift right by filling with zeros


