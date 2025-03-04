class Solution:
    def firstUniqChar(self, s: str) -> int:
        countMap = collections.Counter(s)
        print(countMap)
        for i in range(len(s)):
            if countMap[s[i]] == 1:
                return i
        
        return -1