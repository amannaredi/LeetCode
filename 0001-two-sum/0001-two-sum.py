class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     temp = nums.copy()
        #     temp.remove(nums[i])
        #     if target - nums[i] in temp:
        #         res = []
        #         res.append(i)
        #         if nums.index(target - nums[i]) != i:
        #             res.append(nums.index(target - nums[i]))
        #             return res

        hashMap = {val:i for i, val in enumerate(nums)}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap and hashMap[diff] != i :
                return [i,hashMap[diff]]
        
        return []
                
        