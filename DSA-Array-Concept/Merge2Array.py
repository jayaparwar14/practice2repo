class solution :

    def MergeTwoSortedArray (self,nums1,nums2) :

        n1 = len(nums1)
        n2 = len(nums2)
        result = []
        i = 0
        j = 0

        while i < n1 and j < n2 :

            if(nums1[i] < nums2[j]) :

                if (len(result) == 0 or result[-1] != nums1[i]) :

                    result.append(nums1[i])

                i += 1
            
            else :

                if (len(result) == 0 or result[-1] != nums2[j]) :
                    
                    result.append(nums2[j])

                j += 1

        while i < n1 :

            if (len(result) == 0 or result[-1] != nums1[i]) :
                    
                    result.append(nums1[i])
            i += 1

        while j < n2 :

            if (len(result) == 0 or result[-1] != nums2[j]) :
                    
                    result.append(nums2[j])
            j += 1

        return result

nums1 = [1,1,3,5,7,9]
nums2 = [2,4,4,6,8]

print("Array1 :",nums1) 
print("Array2 :",nums2)
S = solution() 
print("Merge Array1 and Array2 :",S.MergeTwoSortedArray(nums1,nums2))
