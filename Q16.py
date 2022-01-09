n=int(input("Enter the position at which you want to find the number in Fibonacci series:"))
b=1
c=1
for i in range(3,n):
    d = b + c
    b=c
    c=d
print("The number in the Fibonacci series at",n,"th position is :",d)
