# A*B
print("Below is the cartesian product of AxB: ")
for combination in itertools.product(set_a, set_b):
   print(combination)

# set difference
text = input("Enter numbers for the set of A: ")
set_a = text.split()
a = set(set_a)
print(a)
print(" ")
text = input("Enter numbers for the set of B: ")
set_b = text.split()
b = set(set_b)
print(b)
print(" ")
print(a.difference(b))

# Truth value of B is a subset of A


text = input("Enter numbers for the set of A: ")
set_a = text.split()
a = set(set_a)
print(a)
print(" ")
text = input("Enter numbers for the set of B: ")
set_b = text.split()
b = set(set_b)
print(b)
print(" ")

print(a.issubset(b))
