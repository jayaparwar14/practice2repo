class solution :

    def LongestSequenceArray1 (self,nums) :

        n = len(nums) 
        max_count = 0

        for i in range (0,n) :

            num = nums[i] 
            count = 1

            while num + 1 in nums :

                count += 1
                num += 1

            max_count = max(max_count,count) 

        return max_count
    
    def LongestSequenceArray2 (self,nums) :

        n = len(nums) 
        nums.sort()
        longest = 0
        count = 0
        last_smaller = float("-inf")

        for i in range (0,n) :

            num = nums[i]

            if (num - 1 == last_smaller) :

                count += 1
                last_smaller = num

            elif (num != last_smaller) :

                count = 1
                last_smaller = num
            longest = max(longest,count)

        return longest



nums = [1,99,101,98,2,5,3,100,102,1,1]
S = solution()
print(S.LongestSequenceArray1(nums))