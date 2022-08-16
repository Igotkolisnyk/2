cow = int(input("number of cow:"))
a = cow * 4
if cow <= 0:
    a = cow * 0
pig = int(input("number of pig:"))
b = pig * 4
if pig <= 0:
    b = pig * 0
chi = int(input("number of chicken:"))
c = chi * 2
if chi <= 0:
          c = chi * 0
d = a + b + c
print (f"the total number of legs in animals is {d}")
