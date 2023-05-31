class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        return ''.join(word1) == ''.join(word2)
    

obj = Solution()

# Example 1
word1 = ["ab", "c"]
word2 = ["a", "bc"]
# Ex[ected output : true


obj.arrayStringsAreEqual(word1,word2)    