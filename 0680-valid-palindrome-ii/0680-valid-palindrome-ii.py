class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ifPalindrome(s):
            if s == s[::-1]:
                return True
            return False

        l = 0
        r = len(s) - 1
        if s == s[::-1]:
            return True
        else:
            while l <= r :
                new_s = ""
                if s[l] != s[r]:
                    new_s1 = s[:r] + s[r+1:]
                    print(new_s1)
                    new_s2 = s[:l] + s[l+1:] 
                    print(new_s2)
                    return ifPalindrome(new_s1) or ifPalindrome(new_s2)
                l +=1
                r -=1

