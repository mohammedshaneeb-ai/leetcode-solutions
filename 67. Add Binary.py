class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        # Iterate through the strings from right to left
        while i >= 0 or j >= 0 or carry:
            # Get the current digits at positions i and j
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum and carry
            digit_sum = digit_a + digit_b + carry
            carry = digit_sum // 2
            
            # Append the sum digit to the result
            result.append(str(digit_sum % 2))
            
            # Move to the next digits
            i -= 1
            j -= 1
        
        # Reverse the result and join the digits to form a string
        return ''.join(result[::-1])