class solution :

    def UniqueElementArray1 (self,nums) :

        n = len(nums) 
        freq_map = {}

        for i in range (0,n) :

            freq_map[nums[i]] = 0

        j = 0

        for k in freq_map :

            nums[j] = k
            j += 1

        return j
    
    def UniqueElementArray2 (self,nums) :
        # Work only for sorted array and it is optimal solution

        n = len(nums)
        if n == 1 :
            return 1
        
        i = 0
        j = i + 1

        while j < n :

            if (nums[j] != nums[i]) :
                i += 1
                nums[i] , nums[j] = nums[j] , nums[i]

            j += 1
        return i + 1
    
    def UniqueElementArray3 (self,nums) :
        # Work only for sorted array and it is optimal solution

        n = len(nums)
        if n == 1 :
            return 1
        
        i = 0
        
        for j in range (0,n) :

            if (nums[j] != nums[i]) :
                i += 1
                nums[i] , nums[j] = nums[j] , nums[i]

        return i + 1
    
nums = [1,1,1,2,2,3,4,8,8]
S = solution()
print(S.UniqueElementArray3(nums))