a,b,s=0,1,0
n=eval(input("Enter the number of Fibbonaci Numbers you want: "))
print(a,b,end=" ")
for i in range(1,n-1):
    s=a+b
    print(s,end=" ")
    a=b
    b=s
