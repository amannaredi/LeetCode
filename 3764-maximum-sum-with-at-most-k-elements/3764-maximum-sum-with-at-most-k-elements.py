class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        maxVals = []
        for i in range(len(grid)):
            sortedLs = sorted(grid[i])[::-1]
            limit = limits[i]
            for val in sortedLs[:limit]:
                maxVals.append(val)

        sortedMaxVals = sorted(maxVals)[::-1]
        maxSum = sum(sortedMaxVals[:k])

        return maxSum

