class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        maxVals = []
        for i in range(len(grid)):
            sortedLs = sorted(grid[i], reverse = True)
            limit = limits[i]
            maxVals.extend(sortedLs[:limit])

        sortedMaxVals = sorted(maxVals, reverse = True)
        maxSum = sum(sortedMaxVals[:k])

        return maxSum

