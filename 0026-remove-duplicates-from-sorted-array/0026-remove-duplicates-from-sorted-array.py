from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = Counter(nums)
        nums[:len(x)] = [k for k in x.keys()]
    
        return len(x)