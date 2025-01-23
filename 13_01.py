
# print("h")


# # Python program to print "Hello, World!"
# print("Hello, World!")

# Write a Python program to calculate the length of a string.
"""
str=input("your str = ")

print("your str is = ",str)

print(len(str))

# in web:
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('w3resource.com'))

 """

# x=y=z = "helllo"

# print(x)
# print(y)
# print(z)


# x,y,z ="rahat","sajid","imran"
# print(x)
# print(y)
# print(z)

# Fruits = ["mango","banana","lichi"]

# a,b,c=Fruits

# print(a)
# print(c)


# print("hello","world")


# a="hello"
# b="world"

# print(a + b)




# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")


# def greet(name):
#     print("hello,{name}")  
 
#  greet("off")

# [line 57-66 in f string  ]


# x="awesome"

# x = "Hello World"
# x = "Hello World"
# print(x)



# # x = 20	int	
# x = 20
# print(x)
# print(type(x))
# # x = 20.5	float
# x = 20.5
# print(type(x))	
# print(type(x))

# # x = 1j	complex	
# x = 1j
# print(x)
# print(type(x))


# # x = ["apple", "banana", "cherry"]	list	
# x = ["apple","banana","cherry"]
# print(x)
# print(type(x))

# # x = ("apple", "banana", "cherry")	tuple	
# x=("apple","banana","cherry")
# print(x)
# print(type(x))

# # x = range(6)	range	#######

# # x = {"name" : "John", "age" : 36}	dict	
# x ={
#     "name":"Jhon",
#     "age":36
# }
# print(x)
# print(type(x))

# # x = {"apple", "banana", "cherry"}	set	
# x={"apple","banana","cherry"}
# print(x)
# print(type(x))


#  x = frozenset({"apple", "banana", "cherry"})	frozenset #####



# # x = True	bool	
# x=True
# print(x)
# print(type(x))



# x = b"Hello"	bytes	###


# x = bytearray(5)	bytearray	###


# x = memoryview(bytes(5))	memoryview	###


# x = None	NoneType	
# x=None
# print(x)
# print(type(x))


# x = 35e3
# y = 12E4   e== power of 10.
# z = -87.7e100

# print(type(x))
# print(type(y))
# print(type(z))


# import random
# print(random.randrange(9,100))

# a = "Hello, World!"
# print(a[0:]) 
# print(a[:])
# print(len(a))

# Check if "free" is present in the following text:

# txt = "The best things in life are free!"
# # print("free" in txt)
# if "best" in txt:
#     print("fuck off")


# Check if "expensive" is NOT present in the following text:

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# puki = "pukies are awesome"
# print("boom "not in puki)
# print("boom"in puki)


# p="love you"
# if "hate" not in p:
#     print("bainchod")


# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

# H="World!"
# print(H[-5])
# print(H.lower())


# Lower Case
# Example
# The lower() method returns the string in lower case:

# a = "Hello, World!"
# print(a.lower())

# Upper Case
# ExampleGet your own Python Server
# The upper() method returns the string in upper case:

# a = "Hello, World!"
# print(a.upper())


# x=5
# x+=2
# print(x)


# mylist = ['apple', 'banana', 'cherry']
# print(mylist[0])

# x=("pin","cleep","mask")
# y=list(x)
# y[0]="band"
# x=tuple(y)
# print(x)

    #    Convert into a list
# Convert the tuple into a list, add "orange", and convert it back into a tuple:

# thistuple = ("apple", "banana", "cherry")
# y=list(thistuple)
# y.append("orange")
# print(y)

      # Add tuple to a tuple

# thistuple = ("apple", "banana", "cherry")
# y=("orange",)
# thistuple += y
# print(thistuple)

    # Remove Items

# thistuple = ("apple", "banana", "cherry")
# x = list(thistuple)
# x.remove("apple")
# print(x)

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)

