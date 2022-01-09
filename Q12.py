lower = 0
upper = 1000

for num in range(lower , upper + 1):

   

    sum = 0

    temp = num
    while temp > 0:
        rem = temp % 10
        sum += rem ** 3
        temp //= 10

    if num==sum:
       print(num)

