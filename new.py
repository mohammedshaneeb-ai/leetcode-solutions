def searchInsert(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
            break
    
    if target not in arr:
        for i in range(len(arr)-1):
                if target < arr[i]:
                    return i
                    break
                
        return len(arr)
                     


    
nums = [1,3,5,6]
target = 7

print(searchInsert(nums,target))