class solution :

    # Change in original array
    # Brute fros Approach

    def MoveZeroInEndArray1 (self,nums) :

        n = len(nums) 
        temp = []
        
        for i in range (0,n) :

            if (nums[i] != 0) :
                temp.append(nums[i])

        nz = len(temp)

        for i in range (0,nz) :

            nums[i] = temp[i] 

        for i in range (nz,n) :
            nums[i] = 0

    # Optimal Solution

    def MoveZeroInEndArray2 (self,nums) :

        n = len(nums)
        i = 0

        while i < n :

            if (nums[i] == 0) :
                break
            
            i += 1

        if ( i == n) :
            return
         
        j = i + 1

        while j < n :

            if (nums[j] != 0) :
                nums[i] , nums[j] = nums[j] , nums[i] 
                i += 1

            j += 1
        

nums = [1,4,0,5,0,6,7,0,9]
S = solution()
S.MoveZeroInEndArray2 (nums)
print(nums)