#temporary

# a=4
# b=10
# temp=a
# a=b
# b=temp

# print(a,b)


# Tuple unpacking

# a=5
# b=4
# a,b=b,a
# print(a,b)

#arithmetic operators

# a=10
# b=20
# a=a+b
# b=a-b
# a=a-b

# print(a,b)


# n=int(input())
# a,b=0,1

# for _ in range(n):
#     print(a,end=" ")
#     a,b=b,a+b


n=int(input())

i=0
a,b=0,1
while i<=n:
   print(a,end="xxx= ")
   a,b=b,a+b
   i+=1
