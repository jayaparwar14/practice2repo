class Solution :

    def BinarySearch1 (self , nums , target) :

        n = len(nums) 
        low = 0
        high = n - 1

        while low <= high :

            mid = (low + high) // 2

            if (nums[mid] == target) :

                return mid

            elif (nums[mid] < target) :

                low = mid + 1

            else : 

                high = mid - 1


    def BinarySearch2 (self , nums , low , high , target) :

        mid = (low + high) // 2

        if (low > high) :

            return -1

        if (nums[mid] == target) :

            return mid

        elif (nums[mid] < target) :

            self.BinarySearch2 (nums , mid + 1 , high) 

        else :

            self.BinarySearch2 (nums , low , mid - 1)


nums = [1,2,3,4,5,6,7,8,9]

S = Solution ()

print(S.BinarySearch1(nums , 5))
print(S.BinarySearch2(nums , 0 , len(nums) , 5))
