class solution :
     
    def MissingElementInArray1 (self,nums) :

        n = len(nums) 

        for i in range (0,n+1) :
            if i not in nums :
                return i
            
    # Better Solution
    def MissingElementInArray2 (self,nums) :

        n = len(nums) 
        freq = {}

        for i in range (0,n+1) :
            freq[i] = 0

        for num in nums :

            freq[num] = 1
            
        for key , value in freq.items() :

            if (value != 1) :
                return key
            

    # Optimal Solution

    def MissingElementInArray3 (self,nums) :
         
        n = len(nums)                 
        expected_sum = n * (n + 1) // 2   
        actual_sum = sum(nums)

        return expected_sum - actual_sum


nums = [8,3,6,2,1,4,5,0,7]
S = solution() 
print("The missing element in array is :",S.MissingElementInArray1(nums))