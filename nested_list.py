lst=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
lst.append([name,score])
lst.remove(min(lst))  
lst.sort()
print(lst)