#Write a programme that takes as input 2 finite lists of any size, A, B, and outputs the following:
#a) the truth value of B ⊆ A,
#b) a list representing the set A − B,
#c) a list representing the set A × B.
#This is the same question as Question 2 except you are not allowed to use the set environment in
#Python nor are you allowed to use in-built or package Python functions specific to sets which output
#the required sets immediately. You must use lists, for loops, if statements, and other basic Python
#commands.
# E.g. Figure 1 shows the output when the input is A = [1, 4, 2, 5], B = [1, 2, 5]

# A - B
#text is a variable to store user inputs for set A
text = input("Enter numbers for the set of A: ")
#text.split converts the string from the user into a list
set_a = text.split()
#we then assign variable a to store input as a set
a = set(set_a)
print(a)
print(" ")

#text is a variable to store user inputs for set B
text = input("Enter numbers for the set of B: ")
set_b = text.split()
b = set(set_b)
#below we print our set b and they will be separated by a space
print(b)
print(" ")

set_difference = a - b
print("Thus A-B is: ")
print(set_difference)

# B is a subset of A (Truth Value)
text = input("Enter numbers for the set of A: ")
set_a = text.split()

print(set_a)
print(" ")
#below we take input for set B
text = input("Enter numbers for the set of B: ")
#the split function again is used to convert the string to a list
set_b = text.split()

print(set_b)
print(" ")

if set_b <= set_a:
   print("True")
   #'true' will be printed if set_b <= set_a
else:
   print("False")
   # 'false' will be printed if set_b !<= set_a


#below we create two empty sets to store values later in the code
set1 = set()
set2 = set()

#we use a for loop to iterate in asking for user input
#sine we want a finite list we will only loop 3 times as a limit for user input
for i in range(3):
    #we are taking user inputs in a form of integers 3 times of two different set variables
    num1 = int(input("please enter your first positive integer here:"))
    num2 = int(input("please enter your second positive integer here:"))
    #for each iteration we add non repeating values to the sets
    #we used the add function
    set1.add(num1)
    set2.add(num2)

#we print the sets below so that we can see the input from the user
#we specifically use sets because we avoid writting a value twice in a set
print(set1)
print(set2)
#we create empty lists to store values from the sets above
#lists are easy to manipulate in contrast to sets
list1 = []
list2 = []

#we iterate through the sets and take values and assign them to new lists
#values in set1 will be assigned to list1
#values in list2 will be assigned to list2
for i in set1:
    list1.append(i)
for i in set2:
    list2.append(i)

#we print our lists below
print(list1)
print(list2)

#we perform the cartesian product on our lists below
#where m represents items in list 1
#and n represents items in list2
cartesian_product = [[m,n] for m in list1 for n in list2]

#finally below i print the cartesian product of our two lists
print(cartesian_product)


