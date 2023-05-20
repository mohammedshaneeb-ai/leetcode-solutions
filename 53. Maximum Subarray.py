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


def maxSubArray(self, nums):
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

#Example 1
nums = [-2,1,-3,4,-1,2,1,-5,4]
#Expected output : 6

#Example 2
nums = [1]
#Expected output : 1


#Example 3
nums = [5,4,-1,7,8]
#Expected output : 23
