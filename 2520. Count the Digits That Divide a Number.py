class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        num_str = str(num)
        for digit_char in num_str:
            digit = int(digit_char)
            if digit != 0 and num % digit == 0:
                count += 1
        return count
    

obj = Solution()

# Example 1
num = 7
# Expected output: 1

print(obj.countDigits(num))

