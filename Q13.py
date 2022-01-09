num = int(input("Enter the number "))
temp=num
sum=0
order=len(str(num))
while num>0:
   
    rem = num % 10
    sum += rem ** order
    num //= 10

if (temp==sum):
    print(temp,"is an narcissistic number")
else:
    print(temp,"is not an narcissistic number")
   

