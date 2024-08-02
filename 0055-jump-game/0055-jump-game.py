class Solution:
    def canJump(self, nums: List[int]) -> bool:
        run = 0
        for num in nums:
            print(run, num)
            if run < 0:
                return False

            elif num > run:
                run = num
            
            run -=1
        return True
    #    if len(nums) == 1:
    #     return True 
    #    for i in range(nums[0]):
    #     if i == len(nums)-1:
    #         return False
    #     for j in range(1,nums[i]+1):
    #         if i + 1 + j == len(nums):
    #             print(i)
    #             return True
        
    #     continue
    
    #     return False
            
