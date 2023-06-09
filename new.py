def searchInsert(arr,target):
    # checking is there is target is present
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    # if target is not present we are finding the position of target number
    if target not in arr:
        for i in range(len(arr)):
                if target < arr[i]:
                    return i
        return len(arr)
                     

# Example 1
nums = [1,3,5,6]
target = 7
# Expected output 4



# Example 2
nums = [1,3,5,6]
target = 2
# Expected output 1


# Example 3
nums = [1,3,5,6]
target = 5
# Expected output 2


print(searchInsert(nums,target))