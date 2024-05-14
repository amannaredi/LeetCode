class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_ar = 0

        while left<right:
            ar = min(height[left],height[right])*(right - left)
            max_ar = max(max_ar,ar)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1        
        return max_ar  

     