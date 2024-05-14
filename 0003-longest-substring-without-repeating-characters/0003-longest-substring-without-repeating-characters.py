class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        if s.isspace():
            return 1

        res = []
        sub = []
        len_ls = []
        for i in range(len(s)):
            if s[i] not in res:
                res.append(s[i])
                if i == len(s)-1:
                    substr = "".join(res)
                    sub.append(substr)
                    len_ls.append(len(substr))
                    
                    if len(len_ls)==0:
                        return len(substr)
                    else:
                        return max(len_ls) 
                continue

            if s[i] in res:
                substr = "".join(res)
                sub.append(substr)
                len_ls.append(len(substr))
                if res[len(res)-1] == s[i]:
                    res=[]
                else:    
                    idx = res.index(s[i])
                    res = res[idx+1:]
                res.append(s[i])
       
        max_len = max(len_ls)
        return max_len
            