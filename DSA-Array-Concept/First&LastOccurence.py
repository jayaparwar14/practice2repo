class Solution :

    # Brute Force Solution 
    def FirstLastOccurence (slef , nums , target) :

        n = len(nums)
        first = -1
        last = -1

        for i in range (0,n) :

            if (nums[i] == target) :

                if (first == -1) :

                    first = i

                last = i


        return [first , last]

    # Optimal Solution 
    
    def LowerBound (self , nums , target) :

        n = len(nums)
        low = 0
        high = n - 1
        Lower_Bound = n

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


    def FirstLastOccurence2 (self , nums , target) :

        lb = self.LowerBound (nums , target) 

        if (lb == -1) :

            return [-1 , -1]

        ub = self.UpperBound (nums , target)

        return [lb , ub - 1]
    
    


nums = [1,1,1,1,2,2,3,3,4,5,5,6,7,8,8,8,9]

S = Solution ()

print(S.FirstLastOccurence2(nums , 2))