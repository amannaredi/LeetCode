class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currSum = 0
        prefMap = {0:1}
        res = 0
        
        for num in nums:
            
            currSum += num
            
            mod = (currSum % k + k) % k 

            res += prefMap.get(mod,0)
            
            # prefMap[currSum] = prefMap.get(currSum,0) + 1
            prefMap[mod] = prefMap.get(mod,0) + 1
           
        return res 