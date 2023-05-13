class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
    
        # Sort the array of strings to simplify the logic
        strs.sort()
        
        # Consider the first and last strings in the array
        first_str, last_str = strs[0], strs[-1]
        
        common_prefix = ""
        for i in range(len(first_str)):
            if first_str[i] == last_str[i]:
                common_prefix += first_str[i]
            else:
                break
        
        return common_prefix