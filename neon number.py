n=int(input("enter the number= "))
k=n**2
s1=0
while k>0:
    p=int(k%10)
    s1=s1+p
    k=int(k/10)
if(s1==n):
    print("neon number")
else:
    print("not neon number")