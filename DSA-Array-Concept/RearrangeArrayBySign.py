class solution :

    def RearrangeArrayBySign1 (self,nums) :

        n = len(nums) 
        pos = []
        neg = []

        for i in range (0,n) :

            if (nums[i] >= 0) :

                pos.append(nums[i])

            else :

                neg.append(nums[i])

        for i in range (0,len(pos)) :

            nums[2 * i] = pos[i]
            nums[(2 * i) + 1] = neg[i]

        return nums
    

    def RearrangeArrayBySign2 (self,nums) :

        n = len(nums) 
        result = [0] * n
        pos = 0
        neg = 1

        for i in range (0,n) :

            if (nums[i] >= 0) :

                result[pos] = nums[i]
                pos += 2

            else :

                result[neg] = nums[i]
                neg += 2

        return result


nums = [5,10,-3,-1,-10,6]
S = solution()
print(S.RearrangeArrayBySign2(nums))

