class Solution :


    # Duplicates Not Allow

    def SearchRotatedSortedArr1 (self , nums , target) :

        n = len(nums)
        low = 0 
        high = n - 1

        while low <= high :

            mid = (low + high) // 2

            if (nums[mid] == target) :

                return mid

            if (nums[mid] < nums[high]) :

                if (nums[mid] <= target <= nums[high]) :

                    low = mid + 1

                else :

                    high = mid - 1

            else :

                if (nums[low] <= target <= nums[mid]) :

                    high = mid - 1

                else : 

                    low = mid + 1

        return -1

    # Duplicates Allow


    def SearchRotatedSortedArr2 (self , nums , target) :
    
        n = len(nums)
        low = 0 
        high = n - 1
    
        while low <= high :
    
            mid = (low + high) // 2
    
            if (nums[mid] == target) :
    
                return True

            if (nums[low] == nums[mid] == nums[high]) :

                low += 1 
                high -= 1

                continue

            if (nums[mid] < nums[high]) :

                if (nums[mid] <= target <= nums[high]) :

                    low = mid + 1

                else :

                    high = mid - 1

            else :

                if (nums[low] <= target <= nums[mid]) :

                    high = mid - 1

                else :

                    low = mid + 1

        return False



nums1 = [17,18,20,1,3,4,5,7,8,10,11,13,14,16]
nums2 = [1,1,1,1,2,2,3,3,3,3,3,3,4,5,5,6,7,8,8,8,9]


S = Solution ()

print(S.SearchRotatedSortedArr2(nums2 , 3))