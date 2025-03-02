from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        hashMap = Counter(s)
        max_count, char = 0 , ""

        for key, count in hashMap.items():
            if count > max_count:
                max_count = count
                char = key
        
        if max_count > (len(s)+1)//2:
                return ""
        
        res = [""]*len(s)
        idx = 0
        for i in range(max_count):
            res[idx] = char
            idx += 2

        del hashMap[char] 

        for key, value in hashMap.items():
            while value > 0:
                if idx >= len(s):
                    idx = 1
                res[idx] = key
                idx += 2
                value -= 1

        return "".join(res)

            