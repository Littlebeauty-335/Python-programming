n1= int(input("Enter the first number: "))
n2= int(input("Enter the second number: "))
def gcd(n1,n2):
    if(n2==0):
        return n1
    else:
        return gcd(n2,n1%n2)
print("GCD of ", n1," and ",n2," is:- ",gcd(n1,n2))