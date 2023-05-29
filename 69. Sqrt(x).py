def mySqrt(x):
        if x == 0:
            return 0

        left, right = 1, x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return right
# Example 1
x = 4
print(mySqrt(x))
# Expected Output : 2


# Example 2
x = 8
print(mySqrt(x))
# Expected Output : 2

