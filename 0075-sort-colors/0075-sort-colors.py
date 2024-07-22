from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        print(count)
        arr = [0]*3
        s = 0
        for k,v in count.items():
            arr[k] = v

        nums[:arr[0]] = [0 for _ in range(arr[0])]
        nums[arr[0]: arr[0]+arr[1]] = [1 for _ in range(arr[1])]
        nums[arr[0]+arr[1]:] = [2 for _ in range(arr[2])]            
        return nums


