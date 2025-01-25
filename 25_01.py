# WAF to find the factorial n

# i=0
# n=5
# while i <=n:
#     print(n*+i)
#     i+=1


# def calc_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)


# calc_fact(5)
# calc_fact(6)



# WAF to convert USD to BD
# n=input("USD/TK = ")
# p=float(input("total - "))
# def convert(p):
#     if (n=="USD"):
#         print("total tk - ",p*103)
#     if(n=="TK"):
#         print("total dollar - ",p/103)
# convert(p)

# # WAF to convert USD to BD
# n = input("USD/TK = ")
# p = float(input("total - "))

# def convert(p):
#     if n.upper() == "USD":
#         print("Total Tk - ", p * 103)
#     elif n.upper() == "TK":
#         print("Total Dollar - ", p / 103)
#     else:
#         print("Please enter either 'USD' or 'TK' for conversion.")

# convert(p)

# def converter(USD_Val):
#     Taka=USD_Val*103
#     print(USD_Val,"USD  =",Taka,"Taka")


# converter(10)
# converter(12)
# converter(122)
# converter(113)



# n=int(input("number - "))
# def  Number(n):
#     if n%2==0:
#         print("Number is Even")
#     else:
#         print("Number is Odd ")

# Number(n)

# 5>>>1

i=0
n=5
while i<=5:
    print(n,end=",")
    n-=1
    i+=1


n=5
for i in range(0,n+1):
    print(n,end=" ")
    n-=1
    i+=1