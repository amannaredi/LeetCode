class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for element in strs:
            res[tuple(sorted(element))].append(element)
        return list(res.values())
       

                