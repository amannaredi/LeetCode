class Solution:
    def canJump(self, nums: List[int]) -> bool:
        run = 0
        for num in nums:
            print(run, num)
            if run < 0:
                return False

            elif num > run:
                run = max(run, num)
            
            run -=1
        return True
       