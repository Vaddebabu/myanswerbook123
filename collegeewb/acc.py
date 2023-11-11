
n=int(input())
x=n
while x>=10:
    sum=0
    while x>0:
        r=x%10
        sum=sum+(r**2)
        x=x//10
        print(sum)
    x=sum
if x==1:
    print("is a magic number")
else:
    print(n,"its not a magic number")