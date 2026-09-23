class Solution :


    # Average Case

    # Sort in Ascending Order

    def BubbleSort1 (self , nums) :

        n = len(nums)

        for i in range (n-2 , -1 , -1) :

            for j in range (0 , i + 1) :

                if (nums[j] > nums[j + 1]) :

                    nums[j] , nums[j + 1] = nums [j + 1] , nums[j]


    # Sort in Descending Order

    def BubbleSort2 (self , nums) :
    
            n = len(nums)
    
            for i in range (n-2 , -1 , -1) :
    
                for j in range (0 , i + 1) :
    
                    if (nums[j] < nums[j + 1]) :
    
                        nums[j] , nums[j + 1] = nums [j + 1] , nums[j]


    # Best Case
    
    def BubbleSort3 (self , nums) :
    
        n = len(nums)
    
        for i in range (n-2 , -1 , -1) :

            is_swap = False
    
            for j in range (0 , i + 1) :
    
                if (nums[j] > nums[j + 1]) :
    
                    nums[j] , nums[j + 1] = nums [j + 1] , nums[j]
                    is_swap = True

            if (is_swap == False) :
                return 


nums = [1,5,3,7,2,8]

S = Solution()
S.BubbleSort2(nums)
print(nums)

