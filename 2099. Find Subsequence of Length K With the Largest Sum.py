def maxSubsequence(nums,k):
    sub_array = []
    large_index = 0
    for i in range(k):
        largest = nums[0]
        large_index = 0
        j = 0
        k = len(nums)
        while j < k:
            if largest < nums[j+1]:
                largest = nums[j+1]
                large_index = j+1
            k -=1
            j +=1
        print(largest)
        sub_array.append(largest)
        nums.pop(large_index)

    return sub_array

nums = [2,1,3,3]
k = 2



print(maxSubsequence(nums,k))