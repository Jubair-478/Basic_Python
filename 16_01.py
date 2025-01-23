# #print prime numbers between range of 2 to 10 using nested loop:
# i = 0
# while i<=10:
#     for n in range(2,11):
#         if n % 2 ==0:
#             break
#         print(n)
#     i+=1

#print prime numbers between range of 2 to 10 using nested loop:
i = 0
while i <= 10:
    for n in range(2, 11):
        if n % i == 0:
            break
        print(n)
    i += 1
