# WAP to ask the user to enter names of their 3 fav movies and store them in list.

# a=input("first movie- ")
# b=input("second movie- ")
# c=input("third movie- ")
# Movielist=[a,b,c]
# print("Your favourite list is - ",Movielist)
# print(type(Movielist))

# movies=[]
# movies.append(input("First movie - "))
# movies.append(input("Second movie- "))
# movies.append(input("Third movie- "))
# print("your favourite movies are -",movies)



# WAP to check if a list contains a palindrome of elements.(Hint:use copy() method)

list=[1,2,1]
b_list = list.copy()
b_list.reverse()
print(b_list)


if (list==b_list):
    print("It's palindrome")
else:
    print("It's not palindrome")


