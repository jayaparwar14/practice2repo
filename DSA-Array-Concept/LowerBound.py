class Solution :

    def LowerBound (slef , nums , target) :

        n = len(nums) 
        low = 0
        high = n - 1
        lower_bound = n

        while low <= high :

            mid = (low + high) // 2

            if (nums[mid] >= target) :

                lower_bound = mid
                high = mid - 1

            else :

                low = mid + 1

        return lower_bound

nums = [1,1,1,1,2,2,3,3,4,5,5,6,7,8,8,8,9]

S = Solution ()

print(S.LowerBound(nums , 1))


