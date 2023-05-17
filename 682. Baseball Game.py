class Solution:
    def calPoints(self, operations):
        record = []

        for op in operations:
            if op.isdigit() or (op[0] == '-' and op[1:].isdigit()):
                
                record.append(int(op))
            elif op == '+':
                
                record.append(record[-1] + record[-2])
            elif op == 'D':
                
                record.append(record[-1] * 2)
            elif op == 'C':
                
                record.pop()

        return sum(record)

baseball = Solution()

# Example 1
ops = ["5","-2","4","C","D","9","+","+"]


# Example 2
ops = ["1","C"]


print(baseball.calPoints(ops))