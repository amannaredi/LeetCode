class Solution:
    def romanToInt(self, s: str) -> int:
        map_ = {"I" : 1,
        'V' : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,}
        num_l = [i for i in s]
        res = []
        for i in num_l:
            res.append(map_[i])
        print(res)
        sum = 0   
        for i in range(len(res)):
            if i == 0 :
                sum = sum + res[i]
            else:
                if res[i]>res[i-1]:
                    sum = res[i] + sum - 2*res[i-1]
                else:
                    sum = sum + res[i]        
            # sum = sum + res[i]
            # if i == 0 :
            #     if res[i]<res[i+1]:
            #         sum = sum + res[i+1] - res[i]
            #         print(i,sum)
            #     else:
            #         sum = sum +res[i]
            #         print(i,sum)   
            # else:         
            #     if res[i]>res[i-1]:
            #         sum = res[i] + sum - 2*res[i-1]
            #         print(i,sum)
                
            #     else:
            #         sum = sum +res[i]
            #         print(i,sum)
        return sum
        