def my_array(arr,l):
    
    #m=l/2
    for i in range(0,2):
        for j in range(3,l):
            sum=arr[i]+arr[j]
    return sum
    
arr = [1,2,3,4,5,6]
l=len(arr)
for i in range()
print("The sum of the arrays are:",my_array(arr,l))

#################################

# Python program to split array and move first
# part to end.

def splitArr(arr, n, k):
	for i in range(0, k):
		x = arr[0]
		for j in range(0, n-1):
			arr[j] = arr[j + 1]
		
		arr[n-1] = x
		

# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range(0, n):
	print(arr[i], end = ' ')

# Code Contributed by Mohit Gupta_OMG <(0_o)>
