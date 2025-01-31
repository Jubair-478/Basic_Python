# a=500
# b=700

# temp=a
# a=b
# b=temp

# print(a)
# print(b)

# a=2
# b=1

# a=a+b

# b=a-b
# a=a-b

# print(a)
# print(b)


# x=1

# def variable():
#     global x
#     x=5
#     print(x)

# variable()


# n=10
# a,b=0,1
# c=0
# for n in range(0,n+1):
#     print(c,end="  ")
#     a=b
#     b=c
#     c=a+b

# b=(21,34,55)
# C = (0,1,1,2,3,5,8,13,b)
# print(C[0])
# print(C[1])
# print(C[2])
# print(C[3])
# print(C[4])
# print(C[5])
# print(C[6])
# print(C[7])
# print(C[8][0])
# print(C[8][1])
# print(C[8][2])


# a="silent"
# b="listen"

# sorted(a)
# sorted(b)

# print(a,b)



# def are_anagrams(s1, s2):
#     if sorted(s1) == sorted(s2):
#         print(True)
#     else:
#         print(False)

# are_anagrams("listen","silent")
# are_anagrams("xxy","yxx")
# are_anagrams("Exe","Sex")

# A1="Fuck"
# A2="Suck"
# if len(A1) == len(A2):
#     for i in A1:
#         for j in A2:
#             if i == j:
#                 print(True)
#                 break
#             else:
#                 print(False)
#                 break


def anar_koli(S1,S2):
    L1=len(S1)
    L2=len(S2)
    count = 0
    if L1 == L2:
        for i in S1:
            for j in S2:
                if i == j:
                    count +=1
                S1.replace(i,'',1)
                S2.replace(j,'',1)
                break
if count == L1:
    return True
return False



anar_koli("Fuck","Suck")
anar_koli("Listen","Silent")
