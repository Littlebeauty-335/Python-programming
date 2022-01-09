n=int(input("Enter the number:"))

num=0
while(n>0):
        l=len(str(n))
        rem = n % 10
        num = num + rem*(10^(l-1))
        n //= 10

print(num)

