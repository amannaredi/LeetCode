from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # j = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         nums[j] = nums[i]
        #         j += 1
        # print(j)
        # return j
        x = Counter(nums)
        arr = [k for k in x.keys()]
        for i in range(len(arr)):
            nums[i] = arr[i]
        return len(x)