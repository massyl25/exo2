n=int(input("enter a number:"))
def facto(num):
    fact=1
    for x in range(2,n+1):
      fact=fact*x
    return fact

print("your factorial is:"+str(facto(n)))
