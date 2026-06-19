class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch =='[' or ch == '{':
                stack.append(ch)
                continue
            if stack == []:
                return False
            if ch == ')' or ch ==']' or ch == '}':
                temp = stack.pop()
                if (temp == '(' and ch == ')') or (temp == '[' and ch == ']') or (temp == '{' and ch == '}'):
                    pass
                else:
                    return False
        if stack != []:
            return False
        return True