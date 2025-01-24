# WAF to print the length of a list(list is the parameter)
# def length_of_a_list(list):
#     print(len(list))
#     return(list)



# a=[1,2,3,4,5,4,56,677,7867,8]
# codes=[324,454,53465]
# numbers=[723628457,8756865634,8576683684756345]

# length_of_a_list(a)
# length_of_a_list(codes)
# length_of_a_list(numbers)


# WAF to print the elements of a list in a single line.

# def elements_of_list(list):
#     print(list[0:])

# a=[1,2,3,4,5,4,56,677,7867,8]
# codes=[324,454,53465]
# numbers=[723628457,8756865634,8576683684756345]
# hero=["bappa","razzak","jony"]                            #my code


# elements_of_list(a)
# elements_of_list(codes)
# elements_of_list(numbers)
# elements_of_list(hero)

a=[1,2,3,4,5,4,56,677,7867,8]
codes=[324,454,53465]
numbers=[723628457,8756865634,8576683684756345]
hero=["bappa","razzak","jony"]                           


def elements_of_list(list):
    for item in list:
        print(item,end=" ")

 
 
elements_of_list(a)
elements_of_list(codes)
elements_of_list(numbers)
elements_of_list(hero)


