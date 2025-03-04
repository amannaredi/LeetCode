class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = collections.Counter(nums)
        sortedCountMap = [k for k,v in sorted(countMap.items(), key = lambda item: item[1], reverse= True)]
        return sortedCountMap[:k]
            

        
        