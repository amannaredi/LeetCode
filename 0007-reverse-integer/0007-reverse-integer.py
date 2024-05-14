class Solution:
    def reverse(self, x: int) -> int:
        
        if x >0:
            res = int(str(x)[::-1]) 
        else:
            x = abs(x)
            res = -int(str(x)[::-1])
        if res in range(-2**31,2**31):
            return res
        else:
            return 0        
        