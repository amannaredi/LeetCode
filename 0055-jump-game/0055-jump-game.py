class Solution:
    def canJump(self, nums: List[int]) -> bool:
        run = 0
        for num in nums:
            if run < 0:
                return False
            run = max(run, num)
            run -=1
        return True
       