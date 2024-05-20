class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]

        idx_mid = int((0 + len(nums)-1)//2)
        
        mid_num = nums[idx_mid] 
           
        res = []


        if target <= mid_num:
            print("less")
            for i in range(len(nums[:idx_mid + 1])):
                if nums[i] == target:
                    res.append(i)  
        if target >= mid_num:
            for i in range(len(nums[idx_mid+1 :])):
                print("greter")
                if nums[idx_mid+1+i] == target:
                    res.append(idx_mid+1+i)  

                           
        if len(res) == 1:
            res.append(res[0]) 
        if len(res)>=2:
            res = [res[0],res[-1]]     
        else :
            res =  [-1,-1] 

        return res       



        