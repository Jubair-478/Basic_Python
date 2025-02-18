Method 1: Sorting
Method 2: Counting Characters
Method 3: Using a DictionaryMethod 3: Using a Dictionary
Method 4: Frequency ArraysMethod 4: Frequency Arrays
Method 5: XOR ApproachMethod 5: XOR Approach
Method 6: Using Python SetsMethod 6: Using Python Sets


Method 1:
# sorting

def anargram(str1,str2):
   return sorted(str1)==sorted(str2)

print(anargram("YYY","yyy"))
print(anargram("listen","silent"))

x=input().lower()
y=input().lower()

I=sorted(x)
J=sorted(y)
if I == J:
   print("Anargram")
else:
   print("Putki mar")

Method 2:
Counting Characters

from collections import Counter
def anargram(X1,X2):
   return Counter (X1) == Counter(X2)

print(anargram("silent","listen"))

Mehod 3
dictionay
def anargrams(X1,X2):
   if len(X1)!=len(X2):
      return False
   dec={}
   for char in X1:
      if char in dec:
         dec[char]+=1
      else:
         dec[char]=1
   for char in X2:
      if char in dec:
         dec[char]-=1
      else:
         return False

   return all(value == 0 for value in dec.values())

print(anargrams("fuck","suck"))
print(anargrams("listen","silent"))

Method 4: Frequency Arrays
#################################################################################################


Method 6: Using Python Sets Method

def anar(a,b):
    if set(a)==set(b) and len(a)==len(b):
        return True
    return False

print(anar("boob","bboo"))
print(anar("fuck","suck"))

