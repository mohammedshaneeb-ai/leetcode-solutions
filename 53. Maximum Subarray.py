def MaxSubarray(arr):
    sum = float('-inf')
    max = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            max += arr[j]
            if max > sum:
                sum = max
        max = 0
    return sum

print(MaxSubarray([-1]))

#The problem of this code is time limit exceed so i implemented another code see below
