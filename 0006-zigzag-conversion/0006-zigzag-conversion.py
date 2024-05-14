class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        j = 0
        if numRows == 1 or numRows > len(s):
            return s 
        for i in range(len(s)):
            if j == 0:
                res[j].append(s[i])
                curr_j = j
                j = j + 1
            elif j == numRows - 1:
                res[j].append(s[i])
                curr_j = j
                j = j - 1 
            else :
                res[j].append(s[i])  
                if curr_j < j :
                    curr_j = j
                    j = j + 1
                else:
                    curr_j = j
                    j = j - 1            
        ret = []    
        for r in res:
            ret.append("".join(r))

        ret_s = "".join(ret)

        return ret_s