class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        def quickSort(nums):
            if len(nums)<=1:
                return nums

            pivot = nums.pop()
            lower = []
            upper = []
            
            for elem in nums:
                if elem < pivot:
                    lower.append(elem)
                else:
                    upper.append(elem) 
                
            return quickSort(lower) + [pivot] + quickSort(upper)

        sortedNums = quickSort(nums1)
        if len(sortedNums)%2 != 0:
            mid = len(sortedNums)//2
            return float(sortedNums[mid])
        else:
            mid = len(sortedNums)//2
            return (sortedNums[mid-1] + sortedNums[mid])/2


        