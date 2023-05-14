class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


obj = Solution()

#Example 1
x = 121

#Example 2
x = -121

#Example 2
x = 10

