number=int(input("Enter the number: \n"))
def factorial(number):
    fact=1
    for i in range(2,number+1):
        fact*=i
    return fact
print("Factorial of ",number," is :- ",factorial(number))