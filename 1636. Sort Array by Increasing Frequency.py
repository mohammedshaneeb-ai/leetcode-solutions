from collections import Counter

def frequencySort(nums):
    frequency = Counter(nums)

    def custom_sort(a, b):
        if frequency[a] == frequency[b]:
            return b - a  
        return frequency[a] - frequency[b]  
    return sorted(nums, key=lambda x: (frequency[x], -x))


# Example 1 
nums = [2,3,1,3,2]
# Expected output : [1,3,3,2,2]

# Example 2
nums = [1,1,2,2,2,3]
# Expected output : [3,1,1,2,2,2]

# Example 3
nums = [-1,1,-6,4,5,-6,1,4,1]
# Expected output : [5,-1,4,4,-6,-6,1,1,1]


print(frequencySort(nums))
