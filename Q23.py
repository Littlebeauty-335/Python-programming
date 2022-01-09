def my_array(arr,x,n):
    for i in range(0,n):
        if x == arr[i]:
            return 1
        else:
            return 0
            
x=int(input("Enter the number you want to search:"))
arr = [98,23,47,56,111]
n=len(arr)
if my_array(arr,x,n)==1:
    print("The number",x,"is present in the array.")
else:
    print("The number",x,"is not present in the array.")

