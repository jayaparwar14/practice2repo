class solution :

    def SecondLargestElement1 (self,nums) :

        n = len(nums)
        largest = float("-inf")
        secondLargest = float("-inf")

        for i in range (0,n) :
            largest = max(largest,nums[i])
        
        for i in range (0,n) :
            if (nums[i] > secondLargest and nums[i] != largest) :
                secondLargest = nums[i]

        return secondLargest
    
    def SecondLargestElement2 (self,nums) :

        n = len(nums)
        largest = float("-inf")
        SecondLargest = float("-inf")

        for i in range (0,n) :

            if (nums[i] > largest) :
                SecondLargest = largest 
                largest = nums[i]

            elif (nums[i] > SecondLargest and nums[i] != SecondLargest) :
                SecondLargest = nums[i]
                
        return SecondLargest


nums = [2,75,46,53,28,61]

S = solution()
print("The second Largest Element : ",S.SecondLargestElement2(nums))