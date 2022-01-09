def my_array(arr,n,num):
    c=0
    for i in range(n):
        if num==arr[i]:
            c=c+1
    return c

#num=int(input("Enter the number whose frequency you want to find in the array:"))
arr = [1,5,3,1,9,5,11,1,4,3]
n = len(arr)
#for i in range(0,n):
print("The frequency of",1,"in the array is",my_array(arr,n,1))
print("The frequency of",3,"in the array is",my_array(arr,n,3))
print("The frequency of",4,"in the array is",my_array(arr,n,4))
print("The frequency of",5,"in the array is",my_array(arr,n,5))
print("The frequency of",9,"in the array is",my_array(arr,n,9))
print("The frequency of",11,"in the array is",my_array(arr,n,11))

