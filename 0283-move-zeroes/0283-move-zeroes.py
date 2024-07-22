class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = nums.count(0)

        # for _ in range(count):
        #     nums.remove(0)
            
        # for _ in range(count):
            
        #     nums.append(0)
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums
            



