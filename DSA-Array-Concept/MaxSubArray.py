class solution :

    def MaxSubArray1 (self,nums) :

        n = len(nums) 
        maxi = float("-inf") 

        for i in range (0,n) :

            total = 0

            for j in range (i,n) :

                total += nums[j]
                maxi = max(total,maxi) 

        return maxi
    
    def MaxSubArray2 (self,nums) :

        n = len(nums) 
        maxi = float("-inf") 
        total = 0

        for i in range (0,n) :

                total += nums[i]
                maxi = max(total,maxi) 

                if (total < 0) :
                     total = 0

        return maxi

nums = [-2,1,-3,4,-1,2,1,-5,4]   
S = solution()
print(S.MaxSubArray1(nums))