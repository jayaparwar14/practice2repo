class solution :

    def LargestElement (self,nums) :

        n = len(nums)
        largest = nums[0]

        for i in range (0,n) :
            largest = max(largest,nums[i])
        
        return largest

nums = [2,75,46,53,28,61]

S = solution()
print("Largest Element is :",S.LargestElement(nums))