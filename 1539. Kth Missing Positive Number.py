class Solution:
    def findKthPositive(self, arr,k) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            missing_count = arr[mid] - (mid + 1)

            if missing_count >= k:
                right = mid - 1
            else:
                left = mid + 1

        return left + k
