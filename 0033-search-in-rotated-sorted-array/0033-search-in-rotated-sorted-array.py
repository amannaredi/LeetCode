# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         left = 0
#         right = n-1

#         while left <= right:
#             mid = (left+right)//2
#             if nums[mid] > nums[-1]:
#                 left = mid + 1
#             right = mid - 1
        
#         def binarySearch(leftVal, rightVal,target):
#             left, right = leftVal, rightVal
#             while left <= right:
#                 mid = (left + right)//2
#                 if nums[mid] == target:
#                     return mid
#                 elif nums[mid] > target:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
            
#             return -1
        
#         if binarySearch(0,left-1,target) != -1:
#             return binarySearch(0,left-1,target)
        
#         return binarySearch(left,n-1,target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        # Binary search over an inclusive range [left_boundary ~ right_boundary]
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        # Binary search over elements on the pivot element's left
        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer

        # Binary search over elements on the pivot element's right
        return binarySearch(left, n - 1, target)
