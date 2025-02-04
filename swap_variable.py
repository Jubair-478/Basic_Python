# 1. Using a Temporary Variable
# 2.Using Tuple Unpacking
# 3.Using Arithmetic Operations
# 4.Using Bitwise XOR


                                  ###### Using a Temporary Variable #######

# a=5
# b=15
# temp = a
# a=b
# b=temp

# print(a,b)


#                              ######### Using Tuple Unpacking ###
                            
# a = 10
# b = 15

# a,b=b,a

# print(a,b)


# a, b, c = 1, 2, 3
# a, b, c = c, a, b
# print("a:", a, "b:", b, "c:", c)  # Output: a: 3 b: 1 c: 2




#                           ######## Using Arithmetic Operations #####

# a = 25
# b = 35

# a = a+b
# b = a-b
# a = a-b

# print(a,b)
 
                        ####### Using Bitwise XOR ######



                       ####### problems ########


###### You have a list of numbers and you want to swap the positions of two elements. --
#-- Let's say you want to swap the elements at indices 1 and 3 in the list [1, 2, 3, 4]



# lst=[1,2,3,4,]

# i,j = 1,3
# lst[i],[j]=lst[j],[i]

# print(lst)


######## Swapping the First and Last Elements. --
#-- 
# lst = [10, 20, 30, 40]
# i, j = 0, 3  # Indices of the elements to swap
# lst[i], lst[j] = lst[j], lst[i]
# print(lst)  # Output: [40, 20, 30, 10]


######### Using Variables for Indices. --
#-- Using Variables for Indices

# lst = [7, 14, 21, 28]
# first_index = 0
# last_index = len(lst) - 1
# lst[first_index], lst[last_index] = lst[last_index], lst[first_index]
# print(lst)  # Output: [28, 14, 21, 7]

