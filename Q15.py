n = int(input("Enter the number upto which you want to print the fibonacci series:"))
print(0)
b=1
c=1
print(b)
print(c)
for i in range(3,n):
    d = b + c
    b=c
    c=d
    print(d)