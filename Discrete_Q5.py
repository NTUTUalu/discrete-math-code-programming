#we want to take input from user for them to comprise two sets
#we will create an empty set that will take user input

set1 = set()
set2 = set()
#we want to take 3 elements in a list so we will create the limit variable

limit = 3

#now we will use a for loop to get the numbers from user

for i in range(limit):
    #we are taking user inputs in a form of integers 3 times of two different variables
    num1 = int(input("please enter your first positive integer here:"))
    num2 = int(input("please enter your second positive integer here:"))
    #below we are to add the input to the set collection by using add method
    set1.add(num1)
    set2.add(num2)
    #below we check that num1 is divisible by num2,meaning it does not leave a remainder
    #we get true if divisible and does not leave a remainder but false if otherwise
    if num1 % num2 == 0:
        print("True")
    else:
        print("False")

#below we print the result of each iteration for each set
print(set1)
print(set2)