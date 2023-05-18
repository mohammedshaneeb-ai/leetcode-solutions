def lengthOfLastWord( s: str) -> int:
        flag = 0
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                count +=1
                flag = 1
            elif s[i] == ' ' and flag == 1:
                break
        return count

# Example 1
s = "a"
# Expected Output: 1

# Example 2
s = "luffy is still joyboy"
# Expected Output: 6


print(lengthOfLastWord(s))