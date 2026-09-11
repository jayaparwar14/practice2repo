class solution :

    # Change in the original array

    def RotateArrayBy1Place1 (self,nums) :

        n = len(nums) 

        nums[:] = [nums[n-1]] + nums[0 : n-1]
        return nums
    
    def RotateArrayBy1Place2 (self,nums) :

        n = len(nums) 

        temp = nums[n-1]

        for i in range (n-2,-1,-1) :

            nums[i + 1] = nums[i]
        
        nums[0] = temp

        return nums
    
    # Rotate array by place k

    def RotateArrayBykPlace1 (self,nums) :
        
        n = len(nums) 
        k = 3
        rotations = k % n
        
        for _ in range (0,rotations) :
            e = nums.pop()
            nums.insert(0,e)

        return nums
    
    def RotateArrayBykPlace2 (self,nums) :

        n = len(nums)
        k = 5
        rotations = k % n

        nums[:] = nums[n-rotations :] + nums[: n-rotations]

        return nums
    
    def ReverseArray (self,nums,left,right) :
         
         while left < right :
            nums[left] , nums[right] = nums[right]  ,nums[left]
            left += 1
            right -= 1
    
    def RotateArrayBykPlace3 (self,nums,k) :

        n = len(nums)

        if n == 0 :
            return
        
        rotations = k % n

        self.ReverseArray (nums,n-rotations,n-1)
        self. ReverseArray (nums,0,n-rotations-1)
        self. ReverseArray (nums,0,n-1)

        
    
nums = [5,1,9,3,6,2,7]
S = solution() 
S.RotateArrayBykPlace2(nums)
print(nums)

    
