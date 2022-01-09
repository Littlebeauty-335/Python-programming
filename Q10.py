num = int(input("Enter the number "))


def Prime_number(num):
    c=0
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                c+=1
    if (c>1):
         print(num,"is not a prime number")
    else:
        print(num,"is a prime number")

Prime_number(num)
