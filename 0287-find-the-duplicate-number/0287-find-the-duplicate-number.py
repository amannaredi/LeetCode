from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dictionary = Counter(nums)
        for key , value in dictionary.items():
            if value > 1:
                return key
        

