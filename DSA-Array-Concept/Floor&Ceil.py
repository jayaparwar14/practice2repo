class Solution :

    def FloorCeil (slef , nums , target) :

        n = len(nums) 
        low = 0
        high = n - 1
        floor = -1 
        ceil = -1

        while low <= high :

            mid = (low + high) // 2

            if (nums[mid] == target) :

                return [nums[mid] , nums[mid]]

            if (nums[mid] < target) :

                floor = nums[mid]
                low = mid + 1

            else :

                ceil = nums[mid]
                high = mid - 1
                

        return [floor , ceil]

nums = [21,32,43,54,65,76,92,]

S = Solution ()

print(S.FloorCeil(nums , 45))

