from collections import Counter


def frequencySort(nums):
    frequency = Counter(nums)

    def custom_sort(a, b):
        if frequency[a] == frequency[b]:
            return b - a  
        return frequency[a] - frequency[b]  

    # return sorted(nums, key=lambda x: (frequency[x], -x), cmp=custom_sort)
    return sorted(nums, key=lambda x: (frequency[x], -x))


nums = [2,3,1,3,2]
print(frequencySort(nums))
