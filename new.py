def searchInsert(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    if target not in arr:
        for i in range(len(arr)-1):
                if target < arr[i]:
                    return i
                
        return len(arr)
                     

nums = [1,3,5,6]
target = 7

print(searchInsert(nums,target))