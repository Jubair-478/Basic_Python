#Write a recursive function to calculate the sum of first n natural numbers.

def func(n):
    if (n==0):
        return 0
    return n + func(n - 1)


    

print(func(5))




