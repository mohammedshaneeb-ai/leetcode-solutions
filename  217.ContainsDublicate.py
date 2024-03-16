def containsDuplicate(nums):
    return True if len(nums) != len(set(nums)) else  False

nums = [1,2,3,4]
print(containsDuplicate(nums))