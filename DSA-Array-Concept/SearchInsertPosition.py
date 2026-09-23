class Solution :

    def InsertPosition (self , nums ,target ) :

        n = len(nums) 
        low = 0 
        high = n - 1

        while low < high :

            mid = (low + high) // 2

            if (nums[mid] == target) :

                return mid

            if (nums[mid] > target ) :

                high = mid - 1
                

            else :

                low = mid + 1

               
            return low

nums = [1,2,3,4,6,7,8,9]

S = Solution ()

print(S.InsertPosition(nums , 5))


