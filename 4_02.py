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


# n=int(input())

# i=0
# a,b=0,1
# while i<=n:
#    print(a,end=" ")
#    a,b=b,a+b
#    i+=1


# name = "jovan"
# X = name.upper()
# W=sorted(X)
# print(W)

# x=input().lower()
# y=input().lower()

# I=sorted(x)
# J=sorted(y)
# if I == J:
#    print("Anargram")
# else:
#    print("Putki mar")


# def anargram(str1,str2):
#    return sorted(str1)==sorted(str2)

# print(anargram("YYY","yyy"))
# print(anargram("listen","silent"))




# from collections import Counter
# def anargram(X1,X2):
#    return Counter (X1) == Counter(X2)

# print(anargram("silent","listen"))

def anargrams(X1,X2):
   if len(X1)!=len(X2):
      return False
   dec={}
   for char in X1:
      if char in dec:
         dec[char]+=1
      else:
      
    def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
   
   re
#    return all(value == 0 for value in dec.values())

# print(anargrams("fuck","suck"))
# print(anargrams("listen","silent"))

print("pri")




