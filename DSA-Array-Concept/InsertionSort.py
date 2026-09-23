class Solution :

    # Sort in Ascending Order

    def InsertionSort1 (self , nums) :

        n = len (nums)

        for i in range (0,n) :

            j = i - 1
            key = nums[i]

            while j >= 0 and nums[j] > key :

                nums[j + 1] = nums[j] 
                j -= 1

            nums[j + 1] = key


    # Sort in Descending Order

    def InsertionSort2 (self , nums) :
    
            n = len (nums)
    
            for i in range (0,n) :
    
                j = i - 1
                key = nums[i]
    
                while j >= 0 and nums[j] < key :
    
                    nums[j + 1] = nums[j] 
                    j -= 1
    
                nums[j + 1] = key


nums = [8,5,3,7,2,8]

S = Solution()
S.InsertionSort1(nums)
print(nums)

