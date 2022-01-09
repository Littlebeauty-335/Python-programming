n=int(input("Enter the number you want to check:"))
temp=n
sum=0
while n>0:
    fact=1
    rem = n % 10
    #while rem > 0:
    for i in range(0,rem-1):
        fact = fact * (rem-i)
    
    sum = sum + fact 
    n //= 10

if(temp == sum):
    print(temp,"is a strong number.")
else:
    print(temp,"is not a strong number.")