class Solution :

    def MergeArray (self , left , right) :

        result = []
        i = 0 
        j = 0
        n = len(left)
        m = len(right)

        while i < n and j < m : 

            if (left[i] <= right[j]) :

                result.append (left[i])
                i += 1

            else :

                result.append (right[j])
                j += 1

        if i < n :

            while i < n :

                result.append (left[i])
                i += 1

        if j < m :
        
            while j < m :
        
                result.append (right[j])
                j += 1

        return result


    def MergeSort (self , nums) :

        if (len(nums) <= 1) :

            return nums

        mid = len(nums) // 2

        left = nums [ : mid ]
        right = nums [ mid :]

        left = self.MergeSort(left)
        right = self.MergeSort(right)

        return self.MergeArray(left,right)


nums = [1,7,4,9,2,6,8,4]

S = Solution ()

print(S.MergeSort(nums))



                