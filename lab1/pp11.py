a = "KBTU"
print(a[1])

for x in "KBTU":
    print(x)
    
A = "KBTU"
print(len(A))

text = "The best things in life are free!"
print("free" in text)   #True
if "free" in text:
    print("YES, 'free' is present.")
print("good" in text)   #False
if "good" not in text:
    print("NO, 'good' is not present.")
    

b = "Hello"
print(b[1:4])
print(b[:2])
print(b[1:])
print(b[-5:-1])