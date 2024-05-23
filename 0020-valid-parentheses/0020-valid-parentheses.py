class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                elif (stack[-1] == "(" and bracket == ")") or (stack[-1] == "[" and bracket == "]") or (stack[-1] == "{" and bracket == "}"):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
