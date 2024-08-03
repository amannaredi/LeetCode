class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        prefMap = {0:1}
        res = 0
        for num in nums:
            currSum += num
            diff = currSum - k

            res += prefMap.get(diff, 0)
            prefMap[currSum] = prefMap.get(currSum, 0) + 1

        return res