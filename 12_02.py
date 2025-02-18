# arr=[2,3,4,31,32,32,31,7,8,9]
# set(arr)
# print(sorted(set(arr))[-2])

# arr=[1,22,3232,3423,545,3]
# result=sorted(set(arr),reverse=True)
# print(result[1])

# arr=[-10,0,9,10]
# new_set=set(arr)
# new_list=list(new_set)
# new_list.sort()
# print(new_list[-2])

# arr=[4985,84784,9878467,76,467]
# lst=[]
# for i in arr:
#     if i not in lst:
#         lst.append(i)
# lst.sort()
# print(lst[-2])


# arr=[875,8475,874,8475,874857]
# sax=set(arr)
# sax.remove(max(arr))
# print(max(sax))

arr=[1,2,3,3,45,34,3,3,5432,5,243]
lst=[]

for i in arr:
    if i not in lst:
        lst.append(i)
lst.remove(max(lst))
print(max(lst))