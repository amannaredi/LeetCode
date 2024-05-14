class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        sub_str = []
        unique = []
        for i in range(len(s)):
            e = s[i]
            if e in s[i+1:]:
                for j in range(i+1,len(s)):
                    if s[j] == e:
                        str_ = s[i:j+1]
                        if str_  == str_[::-1]:
                            sub_str.append(str_)
            else:
                unique.append(e)                

        # print(sub_str)
        max_len = 0
        res_str = ""
        for i in range(len(sub_str)):
            if len(sub_str[i])>max_len:
                res_str = sub_str[i]
                max_len = len(sub_str[i])
            else:    
                continue
        if len(sub_str)>0:
            return res_str
        else:
            return unique[0]            
                

        