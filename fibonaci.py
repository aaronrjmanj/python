def fab(n):
    a=0
    b=1
    print("The fibonacci series")
    if(n==1):
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
n=int(input("Enter the length of the series: "))
if(n<0):
    print("Invalid negative number")
else:
    fab(n)
print("The End")
