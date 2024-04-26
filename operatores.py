# mehul.thedigitalbusiness@gmail.com

# 1.Write a python program to accept two integers and check whether they are equal or not.
# Test Data : 15 15
# Expected Output :
# Number1 and Number2 are equal

# 2. Write a python program to accept two integers and find maximum.
# Test Data : 7 6 
# Expected Output :
# 7 is greater

# 3.Write a python program to read the roll no, name and marks of three subjects and calculate the total, percentage.
# Test Data :
# Input the Roll Number of the student :1
# Input the Name of the Student :James
# Input the marks of Physics, Chemistry and Computer Application : 70 80 90
# Expected Output :
# Roll No : 1
# Name of Student : James
# Marks in Physics : 70
# Marks in Chemistry : 80
# Marks in Computer Application : 90
# Total Marks = 240
# Percentage = 80.00


# #1. Write a python program to accept two integers and check whether they are equal or not.
num1 = int(input("Enter First Integer : "))
num2 = int(input("Enter Second Integer : "))

if num1==num2:
    print("num1 and num2 are equal")
else:
    print("num1 and num2 are not equal")
    
# 2. Write a python program to accept two integers and find maximum.
def maxnumber(a, b):
    if a > b:
        return a
    else:
        return b
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

max_num = maxnumber(num1, num2)
print("The maximum number is:", max_num)

# 3.Write a python program to read the roll no, name and marks of three subjects and calculate the total, percentage.
