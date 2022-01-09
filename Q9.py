n1= int(input("Enter the first number: "))
n2= int(input("Enter the second number: "))
def power(n1,n2):
    result=1
    for i in range(1,n2+1):
        result*=n1
    return result
print("Result is :- ",power(n1,n2))