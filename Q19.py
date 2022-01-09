Number = int(input("Please Enter any Number: "))    
Num=Number
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    

if(Num==Reverse):
    print("It is a palindrom number")
else:
    print("It is not a palindrom number.")
     
