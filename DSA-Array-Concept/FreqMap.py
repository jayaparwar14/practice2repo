class Solution :

    def AddFreqMap1 (self,nums,x) :

        n = len(nums) 
        freq_map = {}

        for i in range (0,n) :

            if nums[i] in freq_map :

                freq_map[nums[i]] += 1

            else :

                freq_map[nums[i]] = 1

        print(freq_map[x])

    def AddFreqMap2 (self,nums,x) :

        n = len(nums)
        hash_map = {}

        for i in range (0,n) :

            hash_map[nums[i]] = hash_map.get(nums[i],0) + 1

        print(hash_map[x])


nums = [1,4,1,5,2,5,1,6,2,3,4,4,]
S = Solution()
S.AddFreqMap2(nums,1)
