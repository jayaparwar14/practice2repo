class solution :

    def BuySellArray1 (self,nums) :

        n = len(nums)
        max_profit = 0

        for i in range (0,n) :

            for j in range (i+1,n) :

                if(nums[j] > nums[i]) :

                    p = nums[j] - nums[i]
                    max_profit = max(p,max_profit)

        return max_profit
    
    def BuySellArray2 (self,nums) :

        n = len(nums) 
        min_price = float("inf")
        max_price = 0

        for i in range (0,n) :

            min_price = min(min_price,nums[i])
            price = nums[i] - min_price
            max_price = max(min_price,price)

        return max_price

nums = [7,2,1,5,6,4,8]
S = solution()
print(S.BuySellArray1(nums))