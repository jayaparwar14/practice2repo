class Solution :

    def HashNumber (self , nums1 , nums2) :

        for num in nums1 :

            count = 0

            for x in nums2 :

                if x == num :

                    count += 1

            print(count)


nums1 = [11,41,82,51,41,69,32,41,82,41]
nums2 = [11,32,41,69,74,82,90,28,51]

S = Solution()
S.HashNumber(nums1,nums2)