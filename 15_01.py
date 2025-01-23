# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# n=int(input("the number - "))
# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0 and 1<n<6 :
#         print("not weird")
# elif n % 2 == 0 and 5<n<21:
#         print("Weird")
# elif n % 2 == 0 and n>20:
#     print("not weird")

# n=int(input("the number - "))
# if n % 2 != 0 :
#     print("Weird")
# elif n % 2 ==0 and 2<=n<=5:
#     print("Not Weird")
# elif n % 2 ==0 and 6<=n<=20:
#     print("Not Weird")
# elif n % 2 ==0 and n>20:
#     print("Not Weird")
        
# Exercise 1: Print first 10 natural numbers using while loop
# i=1
# while i<=10:
#     print(i)
#     i+=1



# Exercise 2: Print the following pattern
# Write a Python code to print the following number pattern using a loop.

# 1 
# 1 2                                                                           ##################
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


# Exercise 3: Calculate sum of all numbers from 1 to a given number
# Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)


# n = int(input("input the number - "))
# sum_of_num=0
# i=0
# while i <= n:
#     sum_of_num += i 
#     i+=1

# print("total num - ",sum_of_num)


# n = int(input("input the number - "))
# sum_of_num = 0
# i=0
# for i in range(0,(n+1)):
#     sum_of_num+=i
#     i+=1
# print("Total sum - ",sum_of_num)


# Exercise 4: Print multiplication table of a given number
# n=int(input("The number - "))
# i=1
# while i<=10:
#     print(i*n)
#     i+=1

# n=int(input("The number - "))

# for i in range(1,11):
#     print(i*n)
#     i+=1


# Exercise 5: Display numbers from a list using a loop
# Write a Python program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop
# Given:

# numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]
i=0
while numbers[i] % 5 ==0:
    print(i)
    i+=1
    if i <150:
        continue
    elif i <500:
        break
    


# Print 108 using 9 and 12
# Print the number 108 using arithmetic operations on the numbers 9 and 12.
    
# print(12*9)

# Print Learn Coding on CodeChef
# Print "Learn Coding on CodeChef" to the console.

# print("Learn Coding on CodeChef")

# Print Right Angled Triangle
# Print the following pattern (check the sample output):

# *
# **
# ***
# ****
# *****


