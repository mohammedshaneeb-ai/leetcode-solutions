class Solution:
    def gcdOfStrings(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        result = ""

        min_len = min(len1, len2)

        for i in range(1, min_len + 1):
            if len1 % i == 0 and len2 % i == 0:
                substr = str1[0:i]
                if substr * (len1 // i) == str1 and substr * (len2 // i) == str2:
                    result = substr
        return result
    
gcd = Solution()

# Example 1

str1 = "ABCABC" 
str2 = "ABC"
#Expected output: ABC

# Example 2
str1 = "ABABAB"
str2 = "ABAB"
#Expected output: AB

# Example 2
str1 = "LEET"
str2 = "CODE"
#Expected output: ''


print(gcd.gcdOfStrings(str1,str2))
           
