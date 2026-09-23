class Solution :

    # Sort in Ascending Order

    def SelectionSort1 (self , nums ) :
    
        n = len (nums)
    
        for i in range (0,n) :
    
            min_idx = i
    
            for j in range (i + 1,n) :
    
                if (nums[j] < nums[min_idx]) :
    
                    min_idx = j
    
            nums[i] , nums[min_idx] = nums[min_idx] , nums[i]

    # Sort in Descending Order

    def SelectionSort2 (self , nums ) :

        n = len (nums)

        for i in range (0,n) :

            min_idx = i

            for j in range (i + 1,n) :

                if (nums[j] > nums[min_idx]) :

                    min_idx = j

            nums[i] , nums[min_idx] = nums[min_idx] , nums[i]

nums = [1,2,3,8,5,6]
S = Solution()
S.SelectionSort(nums)
print(nums)
                    