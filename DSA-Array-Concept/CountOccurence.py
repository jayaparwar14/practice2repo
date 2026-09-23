class Solution :

    def CountOccurence1 (self , nums , target) :

        n = len(nums) 
        count = 0

        for i in range (0 , n) :

            if (nums[i] == target) :

                count += 1

        return count

    def CountOccurence2 (self , nums , target) :

        n = len(nums) 
        first = -1 
        last = -1 

        for i in range (0 , n) :

            if (nums[i] == target) :

                if (first == -1) :

                    first = i

                last = i

        if (first == -1) :

            return 0

        return last - first + 1


    def LowerBound (self , nums , target) :
    
            n = len(nums)
            low = 0
            high = n - 1
            lower_bound = -1
    
            while low <= high :
    
                mid = (low + high) // 2
    
                if (nums[mid] >= target) :
    
                    lower_bound = mid
                    high = mid - 1
    
                else :
    
                    low = mid + 1
    
            return lower_bound
    
    def UpperBound (self , nums , target) :
        
        n = len(nums)
        low = 0
        high = n - 1
        Upper_Bound = n
        
        while low <= high :
        
            mid = (low + high) // 2
        
            if (nums[mid] > target) :
        
                Upper_Bound = mid
                high = mid - 1
        
            else :
        
                low = mid + 1
        
        return Upper_Bound
    
    
    def CountOccurence3 (self , nums , target) :
    
        lb = self.LowerBound (nums , target) 
    
        if (lb == -1) :
    
            return [-1 , -1]
    
        ub = self.UpperBound (nums , target)
    
        return ub - lb


nums = [1,1,1,1,2,2,3,3,3,3,3,3,4,5,5,6,7,8,8,8,9]

S = Solution ()

print(S.CountOccurence3(nums , 3))