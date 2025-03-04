class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def condition(s):
            return len(set(s)) == 1

        def operation(s):
            res = ""
            for i in range(len(s)-1):
                modulo = (int(s[i])+int(s[i+1]))%10
                res = res + str(modulo)
            
            return res
            
        while len(s)>2:
            s = operation(s)
        
        return condition(s)

