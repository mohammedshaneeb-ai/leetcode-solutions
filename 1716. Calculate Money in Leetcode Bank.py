def totalmoney(n):
    sum = 0
    k=1
    count = 1
    for i in range(1,n+1):
        sum += k
        k +=1
        if i%7 == 0:
            count +=1
            k = count
    return sum


#Example 1
print(totalmoney(20))
#Expected Output: 96


