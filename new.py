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
                     

nums = [1,3,5,6]
target = 7

print(searchInsert(nums,target))