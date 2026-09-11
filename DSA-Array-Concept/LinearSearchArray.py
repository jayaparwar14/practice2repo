class solution :

    def Search (self,nums,target) :

        n = len(nums) 

        for i in range (0,n) :
            if (nums[i] == target) :
                return i
            
            return -1
            
            
nums = [8,2,9,3,5,7,1]
S = solution()
print("Element is Found at the index :",S.Search(nums,5))