class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = []
        for s in strs:
            lens.append(len(s))
        idx = lens.index(min(lens))
        smallest_str = strs[idx]
        res = []
        c = 0
        for e in smallest_str:
            i=0
            while i != len(strs) and c != len(smallest_str) and e == strs[i][c] :
                i+=1
                print(i)
            if i == len(strs):
                print(i)
                res.append(e)
                c +=1
            else:
                break  
              
        pre =  "".join(res)
        length = len(pre)

        for s in strs:
            if s[:length] == pre:
                continue
            else:
                return ""   
        return pre



            




              

        return "".join(res)               

            




        