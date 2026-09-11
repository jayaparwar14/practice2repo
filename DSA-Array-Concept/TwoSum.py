class solution :

    def TwoSumArray1 (self,nums,target) :

        n = len(nums) 

        for i in range (0,n-1) :

            for j in range (1,n) :

                if (nums[i] + nums[j] == target) :
                    return [i,j] 
            
        return -1
    
    def TwoSumArray2 (self,nums,target) :

        n = len(nums) 
        hash_map = {}

        for i in range (0,n) :

            remaining = target - nums[i]

            if remaining in hash_map :

                return [hash_map[remaining],i]
            
            hash_map[nums[i]] = i


nums = [5,9,1,2,4,15,6,3]
S = solution() 
print(S.TwoSumArray2(nums,13))
                
