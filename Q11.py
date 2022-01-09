num = int(input("Enter the number "))
temp=num
sum=0

while temp>0:
    rem = temp % 10
    sum += rem ** 3
    temp //= 10

if (num==sum):
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
   



