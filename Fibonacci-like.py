# n=int(input())
# i=0
# a,b=0,1
# while i<=n:
#     print(a,end="  ")
#     a,b=b,a+b
#     i+=1

n=int(input())
a,b=0,1
for _ in range(n):
    print(a,end="  ")
    a,b=b,a+b