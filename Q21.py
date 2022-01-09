def my_array(arr,n,num):
    c=0
    for i in range(n):
        if num==arr[i]:
            c=c+1
    return c

num=int(input("Enter the number whose frequency you want to find in the array:"))
arr = [1,5,3,1,9,5,11,1,4,3]
n = len(arr)
print("The frequency of",num,"in the array is",my_array(arr,n,num))

