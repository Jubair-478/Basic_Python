"""
Variables:
1. Swap two variables without a third variable. (But that's a common problem, maybe too easy. But 
maybe with some constraint, like not using arithmetic operators.)
Wait, in Python, you can swap with a,b = b,a, but maybe the trick is to do it without that. Hmm. Maybe 
using XOR if they are integers, but that's more of a low-level approach. Not sure if that's Pythonic. 
Alternatively, maybe a problem that involves variable scope inside and outside functions.



2. Predict the output of a code snippet where variables are modified in different scopes. For example, 
global vs local variables.



3. Using variables to unpack tuples in a tricky way, like a, b = b, a + b which is Fibonacci-like. Or maybe 
something with nested tuples.


# problem 1

a=500
b=700

a=a+b

b=a-b
a=a-b

print(a)
print(b)

# problem 2

x=1

def variable():
    global x
    x=5
    print(x)

variable()

# problem 3
n=10
a,b=0,1
c=0
for n in range(0,n+1):
    print(c,end="  ")
    a=b
    b=c
    c=a+b

b=(21,34,55)
C = (0,1,1,2,3,5,8,13,b)
print(C[0])
print(C[1])
print(C[2])
print(C[3])
print(C[4])
print(C[5])
print(C[6])
print(C[7])
print(C[8][0])
print(C[8][1])
print(C[8][2])

"""
# String
   
#    problem -2
# srt ="I am a boy"
# reversed_str=''.join(srt.split()[::-1])
# print(reversed_str)

# problem -3

# def remove_dupli(x):
#     return''.join(sorted(set(x), key=x.index))

# x=input()
# r=remove_dupli(x)
# print(r)
