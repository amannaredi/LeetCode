class Solution:
    def myAtoi(self, s: str) -> int:
        def is32Bit(num):
            return-2**31 <= num <= (2**31) - 1 

        res = []
        nums = [str(i) for i in range(0,10)]
        s = s.strip()

        for i in range(len(s)):
            if s[i] !="-" and s[i] !="+" and s[i]!=" " and s[i] not in nums:
                print("Break", s[i])
                break
            
            if s[i] == "-" and len(res) != 0 :
                break

            if s[i] == "+" and len(res) != 0 :
                break

            if s[i] == " " and len(res) != 0 :
                break
                
            print(s[i])
            res.append(s[i])
            
        print(res)

        if res:
            if len(res) == 1 and (res[0] == "+" or res[0] == "-"):
                return 0

            if res[0] == "-" and len(res)>1:
                num = int("".join(res[1:]))
                if is32Bit(num):
                    return num * (-1)
                else: return -2**31

            if res[0] == "+" and len(res) > 1:
                num = int("".join(res[1:]))
                if is32Bit(num):
                    return num
                else: return 2**31 - 1
            
            else: 
                num = int("".join(res))
                if is32Bit(num):
                    return num
                else: return 2**31 -1
        
        else: 
            return 0
