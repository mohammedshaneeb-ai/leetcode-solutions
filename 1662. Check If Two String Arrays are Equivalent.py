class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:

        return ''.join(word1) == ''.join(word2)
    
obj = Solution()

# Example 1
word1 = ["ab", "c"]
word2 = ["a", "bc"]
# Ex[ected output : true

# Example 2
word1 = ["a", "cb"]
word2 = ["ab", "c"]
# Ex[ected output : false

# Example 3
word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
# Ex[ected output : true

print(obj.arrayStringsAreEqual(word1,word2))    
