class solution :

    def IsArraySorted (self,nums) :

        n = len(nums)

        for i in range (0,n-1) :
            
            if (nums[i] > nums[i+1]) :
                return False 
            
        return True
    
    def ReverseArray (self,nums,left,right) :

        while left < right :
            nums[left] , nums[right] = nums[right]  ,nums[left]
            left += 1
            right -= 1
    
nums = [1,2,3,4,5]
S = solution() 
print(S.IsArraySorted(nums))
S.ReverseArray(nums,0,len(nums)-1)
print(nums)